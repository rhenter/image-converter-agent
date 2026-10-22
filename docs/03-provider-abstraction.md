# Stage 03 — add provider abstraction and deterministic fake provider

Create a small provider layer so the API does not depend on ComfyUI, OpenAI or
any single model.

1. Define a provider protocol/interface with an async or synchronous `generate`
   operation that receives the normalized generation request and returns output
   paths plus provider/model metadata.
2. Implement provider resolution from the configured default and explicit
   request selector. Unknown providers must return a clear 4xx error.
3. Implement a `fake` provider for tests and local contract validation. It must
   be deterministic, create no network request and not pretend to have run a
   real model.
4. Keep providers isolated in their own module(s); avoid a growing conditional
   block in the FastAPI route.
5. Add unit tests for selection, unknown provider and fake-provider behavior.

Run the focused tests, the full test suite and Ruff.
