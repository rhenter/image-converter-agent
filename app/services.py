from dataclasses import dataclass

from sqlalchemy.orm import Session

from app.core.settings import get_settings
from app.models import ImageGenerationRequest
from app.schemas import GenerateImageRequest, GenerateImageResponse


@dataclass(frozen=True)
class GeneratedImage:
    uri: str
    mime_type: str


class ImageProvider:
    name: str

    def generate(self, request: GenerateImageRequest, *, model: str) -> GeneratedImage:
        raise NotImplementedError


class FakeImageProvider(ImageProvider):
    name = "fake"

    def generate(self, request: GenerateImageRequest, *, model: str) -> GeneratedImage:
        return GeneratedImage(
            f"generated://fake/{request.request_id}/image.png", "image/png"
        )


def get_provider(name: str) -> ImageProvider:
    if name == "fake":
        return FakeImageProvider()
    raise ValueError(f"Unsupported image provider: {name}")


def generate_image(
    session: Session, request: GenerateImageRequest
) -> GenerateImageResponse:
    existing = (
        session.query(ImageGenerationRequest)
        .filter_by(external_request_id=request.request_id)
        .one_or_none()
    )
    if existing:
        return GenerateImageResponse(
            request_id=request.request_id,
            status=existing.status,
            provider=existing.provider,
            model=existing.model,
            result_uri=existing.result_uri,
            result_mime_type=existing.result_mime_type,
        )

    settings = get_settings()
    provider_name = request.provider or settings.default_image_provider
    model = request.model or settings.default_image_model
    record = ImageGenerationRequest(
        external_request_id=request.request_id,
        provider=provider_name,
        model=model,
        prompt=request.prompt,
        reference_image_url=str(request.reference_image_url)
        if request.reference_image_url
        else None,
    )
    session.add(record)
    try:
        generated = get_provider(provider_name).generate(request, model=model)
        record.status, record.result_uri, record.result_mime_type = (
            "completed",
            generated.uri,
            generated.mime_type,
        )
        session.commit()
    except Exception as exc:
        record.status, record.error_message = "failed", str(exc)
        session.commit()
        raise
    return GenerateImageResponse(
        request_id=request.request_id,
        status="completed",
        provider=provider_name,
        model=model,
        result_uri=record.result_uri,
        result_mime_type=record.result_mime_type,
    )
