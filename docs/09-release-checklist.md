# Stage 09 — prepare the open-source repository

Review without adding unrelated features.

1. Confirm all changes are provider-neutral and there is no Bota o Shape,
   equipment, catalog, tenant or Django terminology in source or public docs.
2. Add a proposed repository description to the README header:
   `Provider-neutral local image-generation API built with FastAPI, Agno and AgentOS.`
   The GitHub repository description itself can be updated later by the owner.
3. Recommend an open-source license but do not add one without an explicit
   choice from the owner. Suggest Apache-2.0 for a permissive patent grant, or
   MIT for maximum simplicity.
4. Verify `.env`, model files, ComfyUI workflows containing local paths,
   generated images, databases and virtual environments are ignored.
5. Run final tests, Ruff and `git diff --check`.
6. Provide a concise release summary and list any required local setup before
   real Comfy generation.

Do not publish a release or change GitHub settings.
