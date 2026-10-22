# Stage 01 — establish the repository baseline

Work in the `image-converter-agent` repository only.

1. Inspect `README.md`, `pyproject.toml`, `app/`, `tests/`, `.env.example` and
   `.gitignore`.
2. Confirm the service starts from its documented FastAPI entry point and that
   Python requires 3.14 or later.
3. Run `uv run pytest` and `uv run ruff check .` without changing code first.
4. If either command fails because the project is incomplete, make the smallest
   safe correction needed to restore the existing baseline. Do not introduce
   ComfyUI code yet.
5. Ensure `.env` is ignored and `.env.example` contains placeholders only.

Finish by reporting the baseline commands and their result. Do not make a
commit unless explicitly asked.
