from typing import Literal
from uuid import UUID

from pydantic import AnyHttpUrl, BaseModel, Field


class GenerateImageRequest(BaseModel):
    request_id: UUID
    prompt: str = Field(min_length=3, max_length=8_000)
    reference_image_url: AnyHttpUrl | None = None
    provider: str | None = Field(default=None, max_length=64)
    model: str | None = Field(default=None, max_length=128)


class GenerateImageResponse(BaseModel):
    request_id: UUID
    status: Literal["completed", "failed", "pending"]
    provider: str
    model: str
    result_uri: str | None = None
    result_mime_type: str | None = None
