from uuid import uuid4

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.db import Base
from src.schemas import GenerateImageRequest
from src.services import generate_image


def test_generation_is_idempotent() -> None:
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    request = GenerateImageRequest(
        request_id=uuid4(),
        prompt="Minimal technical illustration of a fitness machine",
    )
    with Session(engine) as session:
        first = generate_image(session, request)
        second = generate_image(session, request)
    assert first.status == "completed"
    assert first.result_uri == second.result_uri
