# Stage 06 — expose the service through FastAPI and AgentOS

Complete the API integration while keeping AgentOS bounded.

1. Implement `POST /v1/images/generate` using the schemas and application
   service. Protect it with an optional internal API-key header configured by
   environment variable. Use constant-time comparison where applicable.
2. Return appropriate status codes: validation/authentication errors as 4xx,
   provider/runtime errors as safe 5xx responses. Never expose stack traces.
3. Add a health endpoint that reports readiness without revealing secrets,
   workflow contents or local paths.
4. Keep Agno/AgentOS available for operational introspection only; do not use
   an LLM to generate an image or decide routing. The API endpoint remains
   deterministic and testable.
5. Add OpenAPI descriptions and endpoint tests.

Run the service locally only if its existing start command is documented; do
not invoke a real Comfy generation.
