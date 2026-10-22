# Stage 05 — persist and execute generation requests safely

Wire the provider layer into the application service.

1. Persist generation requests in the existing relational database with
   request id, sanitized input metadata, provider/model, status, output paths,
   timestamps and a safe error message. Never persist API keys or raw secrets.
2. Make a repeated `request_id` idempotent: return the stored completed result,
   or report that an identical request is still running. Reject a conflicting
   reuse of the same id.
3. Use explicit lifecycle states: `pending`, `running`, `succeeded`, `failed`.
4. Ensure provider exceptions update the request to `failed` and generate a
   stable client-facing error response.
5. Keep database access in a repository/service layer, outside FastAPI routes.
6. Add tests covering success, failure and idempotency.

Run the full suite and Ruff.
