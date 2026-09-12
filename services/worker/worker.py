"""Worker process: validate AUTH-25 artefact, then consume queued jobs."""

from __future__ import annotations

import os
import time

from policy_hooks.env_allowlist import WORKER_ENV_ALLOWLIST
from policy_hooks.startup import validate_default


def _store_path() -> str:
    if "ENGINE_STORE_PATH" not in WORKER_ENV_ALLOWLIST:
        return ""
    return os.environ.get("ENGINE_STORE_PATH") or ""


def consume_once() -> list[dict]:
    path = _store_path()
    if not path:
        return []
    import sys
    from pathlib import Path

    api_root = Path(__file__).resolve().parents[1] / "api"
    if str(api_root) not in sys.path:
        sys.path.insert(0, str(api_root))
    from app.store import Store
    from jobs import consume_queued_jobs

    store = Store(path)
    try:
        return consume_queued_jobs(store)
    finally:
        store.close()


def main() -> None:
    validate_default()
    consume_once()
    while True:
        consume_once()
        time.sleep(60)


if __name__ == "__main__":
    main()
