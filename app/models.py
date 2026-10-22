from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class ImageGenerationRequest(Base):
    __tablename__ = "image_generation_requests"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    external_request_id: Mapped[UUID] = mapped_column(unique=True, index=True)
    status: Mapped[str] = mapped_column(String(32), default="pending")
    provider: Mapped[str] = mapped_column(String(64))
    model: Mapped[str] = mapped_column(String(128))
    prompt: Mapped[str] = mapped_column(Text())
    reference_image_url: Mapped[str | None] = mapped_column(Text(), nullable=True)
    result_uri: Mapped[str | None] = mapped_column(Text(), nullable=True)
    result_mime_type: Mapped[str | None] = mapped_column(String(100), nullable=True)
    error_message: Mapped[str | None] = mapped_column(Text(), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
