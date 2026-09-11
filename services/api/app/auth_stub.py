"""Local auth stub for /auth/v1/* via the proxy. Issues HS256 JWTs. No production secrets."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

import jwt
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.config import load_settings

settings = load_settings()
app = FastAPI(title="Engine Labs auth stub")


class TokenRequest(BaseModel):
    sub: str
    grant_version: int = 1
    aal: str = "aal2"


@app.get("/auth/v1/health")
def health() -> dict[str, str]:
    return {"status": "ok" if settings.jwt_secret else "not_configured"}


@app.post("/auth/v1/token")
def token(body: TokenRequest) -> dict[str, str]:
    if not settings.jwt_secret:
        raise HTTPException(status_code=503, detail="SUPABASE_JWT_SECRET not set")
    now = datetime.now(timezone.utc)
    payload = {
        "sub": body.sub,
        "iss": settings.jwt_issuer,
        "aud": settings.jwt_audience,
        "iat": int(now.timestamp()),
        "exp": int((now + timedelta(minutes=15)).timestamp()),
        "role": "authenticated",
        "grant_version": body.grant_version,
        "aal": body.aal,
    }
    return {"access_token": jwt.encode(payload, settings.jwt_secret, algorithm="HS256")}
