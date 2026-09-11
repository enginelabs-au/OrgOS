FROM python:3.11-slim-bookworm
WORKDIR /srv
COPY pyproject.toml uv.lock ./
RUN pip install --no-cache-dir uv && uv sync --frozen --no-dev
COPY adapter ./adapter
COPY policy_hooks ./policy_hooks
COPY config ./config
COPY hermes ./hermes
COPY worker.py ./worker.py
ENV PYTHONPATH=/srv
CMD ["uv", "run", "python", "worker.py"]
