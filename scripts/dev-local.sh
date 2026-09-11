#!/usr/bin/env bash
# Run the OrgOS API without Docker when Compose is unavailable.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
export ENGINE_JWT_ISSUER="${ENGINE_JWT_ISSUER:-http://127.0.0.1:8000/auth/v1}"
export ENGINE_JWT_AUDIENCE="${ENGINE_JWT_AUDIENCE:-authenticated}"
export ENGINE_USAGE_EMIT="${ENGINE_USAGE_EMIT:-0}"
export ENGINE_STORE_PATH="${ENGINE_STORE_PATH:-/tmp/orgos-api-store.sqlite}"
export ENGINE_API_BASE_URL="${ENGINE_API_BASE_URL:-http://127.0.0.1:8000}"
export ENGINE_API_CORS_ORIGINS="${ENGINE_API_CORS_ORIGINS:-http://127.0.0.1:4173,http://127.0.0.1:5173,http://localhost:1420}"
cd services/api
exec uv run uvicorn app.main:app --host 127.0.0.1 --port 8000
