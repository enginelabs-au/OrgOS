# Engine Labs task runner (D-07). `just` is optional; CI uses scripts/ci.sh.

dev:
    bash scripts/dev.sh

test:
    bash scripts/ci.sh test

compose-up:
    docker compose -f infra/compose/docker-compose.yml -f infra/compose/docker-compose.dev.yml up -d

ci:
    bash scripts/ci.sh

seed:
    bash scripts/dev.sh seed

reset:
    bash scripts/dev.sh reset
