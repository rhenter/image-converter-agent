# Image Converter Agent — execution guide

These files are a small, ordered implementation plan for the assistant in
PyCharm. Execute **one file at a time**, in the listed order, from the root of
the `image-converter-agent` repository.

## Ground rules

- This is an open-source, domain-neutral image-generation service. Do not add
  Django, equipment, catalog, tenant, or Bota o Shape business rules.
- Use Python 3.14, `uv`, FastAPI, Agno and AgentOS already present in the
  project. Do not add an LLM dependency unless a stage explicitly needs it.
- Credentials only come from environment variables. Never commit `.env` or a
  real token.
- Prefer explicit provider interfaces over a provider-specific API contract.
- Do not execute ComfyUI generations during automated tests.
- Before each change, inspect the referenced current files. Preserve unrelated
  user changes. At the end of every stage, run only the verification requested
  by that stage and report the changed files.

## Order

1. [01-baseline.md](01-baseline.md)
2. [02-contract-and-settings.md](02-contract-and-settings.md)
3. [03-provider-abstraction.md](03-provider-abstraction.md)
4. [04-comfy-provider.md](04-comfy-provider.md)
5. [05-generation-service.md](05-generation-service.md)
6. [06-api-and-agentos.md](06-api-and-agentos.md)
7. [07-tests-and-docs.md](07-tests-and-docs.md)
8. [08-consumer-integration.md](08-consumer-integration.md)
9. [09-release-checklist.md](09-release-checklist.md)

## Execution protocol

Paste the full contents of the next file into the PyCharm assistant. Do not
combine stages. If a stage fails, fix only that stage before moving on. Stop
and ask for direction if a required secret, exported Comfy workflow, or model
asset is missing.

The repository description and license are intentionally deferred; stage 09
records what is needed before publishing a release.
