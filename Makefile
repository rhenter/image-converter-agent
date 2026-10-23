HOST ?= 127.0.0.1
PORT ?= 8000

.PHONY: agentos start test lint lock

agentos: deps
	uv run uvicorn src.main:app --host $(HOST) --port $(PORT) --reload

start: agentos


test:
	uv run pytest -vv

lint:
	uv run ruff check .

lock:
	uv lock
