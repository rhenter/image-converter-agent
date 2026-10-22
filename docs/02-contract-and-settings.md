# Stage 02 — define the generic image-generation contract

Implement a provider-neutral HTTP contract. This service must not know about
equipment, PDFs, catalogs, tenants or Django.

1. Add typed request/response schemas for `POST /v1/images/generate`:
   - `request_id` UUID, supplied by the caller or generated safely.
   - `prompt` string.
   - optional `reference_image_url` and optional absolute
     `reference_image_path`; exactly zero or one is allowed.
   - optional `provider` and `model` selectors.
   - response includes request id, status, provider, model and generated
     absolute local paths.
2. Add settings through `pydantic-settings`, all configured by environment
   variables. Include provider selection, an internal API key, allowed local
   input roots, output root, timeout and log level.
3. Reject a local path outside configured allowed input roots. Do not accept
   arbitrary file-system paths.
4. Update `.env.example` with safe placeholder values only.
5. Add focused validation tests.

Keep the endpoint implementation minimal for now. Run `uv run pytest` and
`uv run ruff check .`.
