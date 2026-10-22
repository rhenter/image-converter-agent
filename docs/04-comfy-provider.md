# Stage 04 — implement the local ComfyUI provider

Implement a `comfy` provider without embedding a model, node id or workflow in
Python code.

1. Read Comfy configuration exclusively from environment variables:
   `COMFY_BASE_URL`, `COMFY_WORKFLOW_PATH`, `COMFY_INPUT_ROOT`,
   `COMFY_OUTPUT_ROOT`, timeout and poll interval.
2. Load an exported ComfyUI **API-format** workflow JSON. Support only these
   placeholders inside node input values:
   - `{{reference_image}}`
   - `{{prompt}}`
   - `{{output_prefix}}`
3. For a local reference image, verify its allowed path, upload it to ComfyUI's
   image endpoint, then substitute its uploaded name. URL input may be deferred
   with a clear validation error; do not silently download remote files.
4. Submit the resolved graph to `/prompt`, poll `/history/{prompt_id}`, and
   extract output images from the completed history.
5. Return only absolute paths under `COMFY_OUTPUT_ROOT`; reject traversal or
   paths outside that root. Include bounded timeouts and useful failure errors.
6. Write HTTP-mocked tests for upload, prompt submission, completed history,
   failure and timeout. Tests must not require ComfyUI or GPU hardware.

Do not alter the generic public contract. Run tests and Ruff.
