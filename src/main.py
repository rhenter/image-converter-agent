import hmac
from typing import Annotated

from agno.db.sqlite import SqliteDb
from agno.os import AgentOS
from fastapi import Depends, FastAPI, Header, HTTPException, status
from sqlalchemy.orm import Session

from src.core.settings import get_settings
from src.db import get_session
from src.schemas import GenerateImageRequest, GenerateImageResponse
from src.services import generate_image

base_app = FastAPI(title="Image Generation Provider", version="0.1.0")
SessionDependency = Annotated[Session, Depends(get_session)]


def require_internal_key(x_internal_api_key: str = Header()) -> None:
    if not hmac.compare_digest(x_internal_api_key, get_settings().internal_api_key):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid internal key"
        )


@base_app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@base_app.post(
    "/v1/images/generate",
    response_model=GenerateImageResponse,
    dependencies=[Depends(require_internal_key)],
)
def generate_image_endpoint(
    payload: GenerateImageRequest, session: SessionDependency
) -> GenerateImageResponse:
    return generate_image(session, payload)


agent_os = AgentOS(
    id="image-generation-provider",
    base_app=base_app,
    db=SqliteDb(db_file="agentos.db"),
    telemetry=False,
)
app = agent_os.get_app()
