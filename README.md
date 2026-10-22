# Bota o Shape Agent Service

Serviço interno para transformar referências de catálogo em ilustrações padronizadas de equipamentos.

- A API Django é a fonte de verdade de equipamentos, tenants e arquivos finais.
- Este serviço tem banco próprio para requisições e rastreabilidade, sem FKs para a API.
- `POST /v1/equipment-images/generate` exige `X-Internal-Api-Key`.
- `provider` e `model` podem ser definidos por requisição: o domínio não fica preso a um modelo de IA.
- A implementação inicial usa o provider `fake`, sem chamar IA nem consumir créditos.
- `request_id` garante idempotência.
- Agno AgentOS é executado localmente na mesma aplicação FastAPI.

## Desenvolvimento

```bash
cp .env.example .env
uv run uvicorn app.main:app --reload
uv run pytest
uv run ruff check .
```

Para produção, configure `DATABASE_URL` para PostgreSQL. O próximo passo é inserir providers reais atrás de `ImageProvider`, armazenar o arquivo retornado e derivar o thumbnail localmente.

