"""JWT verification (issuer/audience/secret) and grant_version check."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

import jwt
from fastapi import Header, HTTPException, Request

from app.config import Settings
from app.store import Store

MAX_TOKEN_SECONDS = 15 * 60 + 30


@dataclass
class AuthContext:
    principal_id: str
    tenant_id: str
    grant_version: int
    claims: dict[str, Any]


def decode_token(token: str, settings: Settings) -> dict[str, Any]:
    if not settings.jwt_secret:
        raise HTTPException(status_code=503, detail="jwt secret not configured")
    try:
        claims = jwt.decode(
            token,
            settings.jwt_secret,
            algorithms=["HS256"],
            audience=settings.jwt_audience,
            issuer=settings.jwt_issuer,
        )
    except jwt.PyJWTError as exc:
        raise HTTPException(status_code=401, detail=f"invalid token: {exc}") from exc
    iat = claims.get("iat")
    exp = claims.get("exp")
    if iat is not None and exp is not None and int(exp) - int(iat) > MAX_TOKEN_SECONDS:
        raise HTTPException(status_code=401, detail="token lifetime exceeds 15 minutes")
    return claims


def authenticate(request: Request, authorization: str | None) -> AuthContext:
    settings: Settings = request.app.state.settings
    store: Store = request.app.state.store
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=401, detail="missing bearer token")
    claims = decode_token(authorization.split(" ", 1)[1].strip(), settings)
    principal_id = str(claims.get("sub") or "")
    if not principal_id:
        raise HTTPException(status_code=401, detail="token missing sub")
    principal = store.principal(principal_id)
    token_gv = int(claims.get("grant_version", principal["grant_version"]))
    if token_gv != int(principal["grant_version"]):
        raise HTTPException(status_code=401, detail="grant_version mismatch")
    return AuthContext(
        principal_id=principal_id,
        tenant_id=principal["tenant_id"],
        grant_version=int(principal["grant_version"]),
        claims=claims,
    )


def auth_dep(request: Request, authorization: str | None = Header(default=None)) -> AuthContext:
    return authenticate(request, authorization)


def require_reauth(ctx: AuthContext) -> None:
    reauth_at = ctx.claims.get("reauth_at")
    if not reauth_at:
        raise HTTPException(status_code=401, detail="reauthentication required")
    now = datetime.now(timezone.utc).timestamp()
    if now - float(reauth_at) > 300:
        raise HTTPException(status_code=401, detail="reauthentication expired")
