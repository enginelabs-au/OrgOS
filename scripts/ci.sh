#!/usr/bin/env bash
# Product CI entry (D-07). Does not require `just`.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
MODE="${1:-all}"

run_js() {
  if [[ -f package-lock.json ]]; then
    npm ci --ignore-scripts
  else
    npm install --ignore-scripts
  fi
  npm test
}

run_py() {
  if command -v uv >/dev/null 2>&1; then
    (cd services/api && uv sync --frozen || uv sync)
    (cd services/api && uv run pytest -q)
    (cd services/worker && uv sync --frozen || uv sync)
    (cd services/worker && uv run pytest -q)
  else
    echo "uv missing; skip python" >&2
    return 1
  fi
}

run_audits() {
  if command -v npm >/dev/null 2>&1 && [[ -f package-lock.json ]]; then
    npm audit --audit-level=high || true
  fi
  if command -v pip-audit >/dev/null 2>&1; then
    (cd services/api && pip-audit) || true
    (cd services/worker && pip-audit) || true
  else
    echo "pip-audit not installed; skip"
  fi
}

run_compose() {
  python3 infra/compose/tests/compose_assertions.py
}

case "$MODE" in
  test)
    run_js
    run_py
    ;;
  all)
    run_js
    run_py
    run_compose
    run_audits
    ;;
  js) run_js ;;
  py) run_py ;;
  compose) run_compose ;;
  *)
    echo "usage: $0 [all|test|js|py|compose]" >&2
    exit 2
    ;;
esac
