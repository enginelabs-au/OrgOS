#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
CMD="${1:-up}"

case "$CMD" in
  up)
    if docker info >/dev/null 2>&1; then
      docker compose -f infra/compose/docker-compose.yml -f infra/compose/docker-compose.dev.yml up -d
      bash "$ROOT/scripts/port-scan.sh" http://127.0.0.1:8080/health || true
    else
      echo "Docker unavailable; using local API (scripts/dev-local.sh). Start it in another terminal, then: bash scripts/port-scan.sh http://127.0.0.1:8000/health"
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
