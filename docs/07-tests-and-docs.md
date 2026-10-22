# Stage 07 — complete quality checks and documentation

Make the independent service usable by another application.

1. Update `README.md` with purpose, architecture, Python 3.14 setup, `uv`
   commands, environment setup, API example, fake provider workflow and Comfy
   configuration.
2. Document how to export a ComfyUI workflow as API JSON and replace the three
   supported placeholders. Do not include copyrighted model files or real
   credentials.
3. Describe output-path semantics and the shared-local-filesystem requirement.
4. Add a concise threat-model section: API key, allowed input roots, output
   root validation, local-only Comfy endpoint, no credential logging.
5. Ensure tests cover all providers via mocks and no test depends on a GPU,
   network or local developer files.
6. Run `uv run pytest`, `uv run ruff check .`, and any formatter already used
   by the project.

Report any coverage gap instead of weakening a configured threshold.
