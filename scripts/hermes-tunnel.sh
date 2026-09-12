#!/usr/bin/env bash
# Background SSH tunnels to Hermes on the VPS.
# :9119 = desktop serve UI (login). :8642 = HTTP API server.
# Uses ~/.ssh/config Host hermes-vps. No .env required.
set -euo pipefail
exec ssh -N -o BatchMode=yes -o RequestTTY=no \
  -o ServerAliveInterval=25 -o ServerAliveCountMax=6 \
  -L 127.0.0.1:9119:127.0.0.1:9119 \
  -L 127.0.0.1:8642:127.0.0.1:8642 \
  hermes-vps
