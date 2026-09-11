#!/usr/bin/env bash
# Prove which OrgOS local ports answer. Used when Docker Compose is unavailable.
set -euo pipefail
TARGETS="${*:-http://127.0.0.1:8000/health http://127.0.0.1:8001/health http://127.0.0.1:8080/health}"
fail=0
for url in $TARGETS; do
  if curl -fsS --max-time 3 "$url" >/dev/null; then
    echo "PASS $url"
  else
    echo "FAIL $url"
    fail=1
  fi
done
exit "$fail"
