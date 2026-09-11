#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
CMD="${1:-up}"

case "$CMD" in
  up)
    if docker info >/dev/null 2>&1; then
      docker compose -f infra/compose/docker-compose.yml -f infra/compose/docker-compose.dev.yml up -d
    else
      echo "Docker unavailable; start API locally with: (cd services/api && uv run uvicorn app.main:app --reload --port 8000)"
    fi
    ;;
  seed)
    (cd services/api && uv run python -m app.seed)
    ;;
  reset)
    docker compose -f infra/compose/docker-compose.yml -f infra/compose/docker-compose.dev.yml down -v || true
    rm -f /tmp/engine-labs-api-store.json
    ;;
  *)
    echo "usage: $0 [up|seed|reset]" >&2
    exit 2
    ;;
esac
