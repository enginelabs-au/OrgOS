"""Structured JSON logs with trace_id."""

from __future__ import annotations

import json
import logging
import sys
import time
import uuid
from typing import Any

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        payload: dict[str, Any] = {
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
            "time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }
        if hasattr(record, "trace_id"):
            payload["trace_id"] = record.trace_id
        if record.exc_info:
            payload["exc"] = self.formatException(record.exc_info)
        return json.dumps(payload, separators=(",", ":"))


def configure_logging() -> logging.Logger:
    logger = logging.getLogger("engine.api")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(JsonFormatter())
        logger.addHandler(handler)
    logger.propagate = False
    return logger


class TraceMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, logger: logging.Logger) -> None:  # type: ignore[no-untyped-def]
        super().__init__(app)
        self.logger = logger

    async def dispatch(self, request: Request, call_next) -> Response:  # type: ignore[no-untyped-def]
        trace_id = request.headers.get("x-trace-id") or uuid.uuid4().hex
        request.state.trace_id = trace_id
        extra = {"trace_id": trace_id}
        self.logger.info("%s %s", request.method, request.url.path, extra=extra)
        response = await call_next(request)
        response.headers["x-trace-id"] = trace_id
        self.logger.info(
            "complete %s %s %s",
            request.method,
            request.url.path,
            response.status_code,
            extra=extra,
        )
        return response
