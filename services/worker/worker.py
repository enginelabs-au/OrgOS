"""Worker process: validate AUTH-25 artefact, then idle until jobs arrive."""

from __future__ import annotations

import time

from policy_hooks.startup import validate_default


def main() -> None:
    validate_default()
    while True:
        time.sleep(60)


if __name__ == "__main__":
    main()
