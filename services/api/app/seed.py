"""Seed founder org, founder seat, 43 registry rows, empty ledger."""

from __future__ import annotations

import os

from app.config import load_settings
from app.store import Store


def main() -> None:
    settings = load_settings()
    path = os.environ.get("ENGINE_STORE_PATH", settings.store_path)
    store = Store(path)
    store.seed_founder()
    store.close()
    print(f"seeded store at {path}")


if __name__ == "__main__":
    main()
