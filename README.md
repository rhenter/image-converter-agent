# Image Converter Agent

[![CI](https://github.com/rhenter/image-converter-agent/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/rhenter/image-converter-agent/actions/workflows/ci.yml)
[![Coverage](badges/coverage.svg)](https://github.com/rhenter/image-converter-agent/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.14-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.156.8-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Agno](https://img.shields.io/badge/Agno-3.1%2B-F97316)](https://docs.agno.com/)
[![AgentOS](https://img.shields.io/badge/AgentOS-Agno-F97316)](https://docs.agno.com/agent-os/introduction)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-supported-4169E1?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![uv](https://img.shields.io/badge/uv-package%20manager-DE5FE9)](https://docs.astral.sh/uv/)
[![pytest](https://img.shields.io/badge/tests-pytest-0A9EDC?logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Ruff](https://img.shields.io/badge/lint-Ruff-D7FF64?logo=ruff&logoColor=black)](https://docs.astral.sh/ruff/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Provider-neutral local API for image generation, built with FastAPI, Agno, and AgentOS.

The project provides a generic image-generation contract. The initial provider is `fake`, which is suitable for development and testing without a GPU, credits, or external services. Real providers can be added behind the `ImageProvider` interface.

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/)
- PostgreSQL for persistent environments; SQLite is used by default and in tests

## Installation

```bash
git clone https://github.com/rhenter/image-converter-agent.git
cd image-converter-agent
uv sync
cp .env.example .env
```

Edit `.env` when you need PostgreSQL or a different internal API key. The default values start the service locally with SQLite and the `fake` provider.

## Development

Start the API:

```bash
uv run uvicorn src.main:app --reload
```

Interactive documentation is available at <http://127.0.0.1:8000/docs>.

Run the tests and linter:

```bash
uv run pytest
uv run ruff check .
```

The same commands are available in the Makefile:

```bash
make test
make lint
```

## API

Check the application:

```bash
curl http://127.0.0.1:8000/health
```

Generate an image using the local test provider:

```bash
curl -X POST http://127.0.0.1:8000/v1/images/generate \
  -H 'Content-Type: application/json' \
  -H 'X-Internal-Api-Key: development-only-key' \
  -d '{
    "request_id": "00000000-0000-0000-0000-000000000001",
    "prompt": "A simple blue mug on a white background"
  }'
```

`request_id` makes the operation idempotent. `provider` and `model` can be sent per request; when omitted, they are read from `DEFAULT_IMAGE_PROVIDER` and `DEFAULT_IMAGE_MODEL`.

## Structure

```text
src/
├── core/settings.py  # Environment-based configuration
├── db.py             # SQLAlchemy sessions
├── main.py           # FastAPI and AgentOS
├── models.py         # Request persistence
├── schemas.py        # Input and output contracts
└── services.py       # Providers and image generation
tests/                # API and service tests
docs/                 # Contracts and implementation decisions
```

## CI and coverage

GitHub Actions runs the tests and Ruff on every push to `main`, pull request, or manual execution. After a push to `main`, the workflow updates `badges/coverage.svg` with locally calculated coverage, following the model used by [Canhoto Simples](https://github.com/rhenter/canhoto_simples_api).

## Contributing

Contributions are welcome. Please open an issue to discuss a significant change before submitting a pull request. For smaller changes, fork the repository, create a focused branch, run the tests and linter, and open a pull request with a clear description of the change.

## License

This project is available under the [MIT License](LICENSE).
