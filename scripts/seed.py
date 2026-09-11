#!/usr/bin/env python3
"""Seed founder org, founder seat, 43 registry rows, empty ledger."""

from __future__ import annotations

import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API = ROOT / "services" / "api"
sys.path.insert(0, str(API))
runpy.run_module("app.seed", run_name="__main__")
