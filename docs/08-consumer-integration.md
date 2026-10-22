# Stage 08 — publish the consumer integration contract

Do not modify the Bota o Shape API in this stage. Produce only integration
documentation and examples for its future management command.

1. Add `docs/consumer-contract.md` describing the request to
   `POST /v1/images/generate`, including API-key header, local reference image
   path, drawing prompt and response shape.
2. State that a consumer must first validate/crop its own source image, send a
   request for each variant (for example thumbnail and detail), and persist the
   returned paths in its own JSON manifest.
3. State explicitly that the provider service does not create equipment,
   process PDFs, identify catalog pages, know tenants or write into another
   application's database.
4. Include a short `curl` example using placeholders, never a real API key.

Run documentation-related checks only if the repository has them.
