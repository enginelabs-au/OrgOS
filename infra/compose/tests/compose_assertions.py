#!/usr/bin/env python3
"""Assert Compose topology: only proxy publishes a host port; worker is not on data."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = [ROOT / "docker-compose.yml", ROOT / "docker-compose.dev.yml"]
SERVICE_FIELDS = {
    "image",
    "build",
    "ports",
    "networks",
    "environment",
    "env_file",
    "depends_on",
    "healthcheck",
    "expose",
    "command",
    "volumes",
    "working_dir",
    "profiles",
    "restart",
    "user",
    "entrypoint",
    "labels",
    "privileged",
    "cap_drop",
    "cap_add",
}


def parse_services(text: str) -> dict[str, dict]:
    services: dict[str, dict] = {}
    section = None
    current = None
    current_key = None
    for raw in text.splitlines():
        if raw.strip().startswith("#"):
            continue
        if not raw.startswith(" ") and raw.endswith(":"):
            section = raw[:-1].strip()
            current = None
            current_key = None
            continue
        if section != "services":
            continue
        if raw.startswith("  ") and not raw.startswith("    ") and raw.strip().endswith(":"):
            key = raw.strip()[:-1]
            current = key
            services.setdefault(current, {"ports": False, "networks": [], "has_ports_key": False})
            current_key = None
            continue
        if current and raw.startswith("    ") and not raw.startswith("      ") and raw.strip().endswith(":"):
            current_key = raw.strip()[:-1]
            if current_key == "ports":
                services[current]["has_ports_key"] = True
                services[current]["ports"] = True
            continue
        if current and current_key == "networks" and raw.strip().startswith("- "):
            services[current]["networks"].append(raw.strip()[2:].strip())
        if current and current_key == "ports" and raw.strip().startswith("- "):
            services[current]["ports"] = True
    return services


def main() -> int:
    errors: list[str] = []
    for path in FILES:
        if not path.exists():
            errors.append(f"missing {path}")
            continue
        services = parse_services(path.read_text())
        if path.name == "docker-compose.yml":
            for required in ("proxy", "api", "worker", "postgres"):
                if required not in services:
                    errors.append(f"{path.name}: missing service {required}")
            if "worker" in services:
                nets = services["worker"]["networks"]
                if "data" in nets:
                    errors.append("worker must not join the data network (D-08 / C-02)")
                if nets != ["worker"]:
                    errors.append(f"worker networks must be only ['worker'], got {nets}")
            for name, spec in services.items():
                if spec["ports"] and name != "proxy":
                    errors.append(f"{path.name}: {name} publishes a host port; only proxy may")
            if "proxy" in services and not services["proxy"]["ports"]:
                errors.append("proxy must publish a host port")
        if path.name == "docker-compose.dev.yml":
            for name, spec in services.items():
                if spec["ports"] and name != "proxy":
                    errors.append(f"{path.name}: {name} publishes a host port; only proxy may")
    if errors:
        print("compose assertions FAILED:")
        for err in errors:
            print(f"  - {err}")
        return 1
    print("compose assertions passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
