"""Engine Labs API — phase 1 foundation."""

from __future__ import annotations

import hashlib
import hmac
import json
import os
import time
from typing import Any

from fastapi import Depends, FastAPI, HTTPException, Query, Request
from fastapi.responses import JSONResponse, StreamingResponse

from app.auth import AuthContext, auth_dep, require_reauth
from app.config import load_settings
from app.github_app import GithubError, installation_permissions, list_pulls, open_pull, probe_github
from app.github_grants import intersect_repo_grants, may_open_pull
from app.hermes_health import probe_hermes
from app.loop import LOOP_STAGES
from app.grants import effective_grants
from app.logging_util import TraceMiddleware, configure_logging
from app.store import Store, StoreError
from app.usage import emit_usage, validate_usage_event

SIGNED_URL_TTL = 300

logger = configure_logging()


def create_app(store_path: str | None = None) -> FastAPI:
    settings = load_settings()
    if store_path:
        settings = type(settings)(**{**settings.__dict__, "store_path": store_path})
    store = Store(settings.store_path)
    store.seed_founder()

    app = FastAPI(title="Papership API", version="0.1.0")
    app.state.settings = settings
    app.state.store = store
    app.add_middleware(TraceMiddleware, logger=logger)

    @app.exception_handler(StoreError)
    async def store_error(_request: Request, exc: StoreError) -> JSONResponse:
        return JSONResponse({"detail": str(exc)}, status_code=exc.status_code)

    @app.exception_handler(GithubError)
    async def github_error(_request: Request, exc: GithubError) -> JSONResponse:
        return JSONResponse({"detail": exc.detail}, status_code=exc.status_code)

    @app.get("/health")
    def health() -> dict[str, Any]:
        db = store.health_db()
        dbos = "ok" if db == "ok" else "error"
        hermes = probe_hermes(settings.hermes_api_base_url)
        github = probe_github(
            settings.github_app_id,
            settings.github_installation_id,
            settings.github_private_key_path,
            live=not settings.test_hooks,
        )
        return {
            "status": "ok" if db == "ok" else "degraded",
            "db": db,
            "dbos": dbos,
            "worker_config": "ok",
            "hermes": hermes,
            "hermes_pin": settings.hermes_version_pin,
            "usage_emit": settings.usage_emit,
            "github": github,
        }

    @app.get("/registry")
    def registry(_ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        items = store.list_registry()
        return {
            "items": items,
            "count": len(items),
            "hermes_side_effecting_tools": "catalogued",
            "loop_stages": list(LOOP_STAGES),
        }

    @app.get("/seats/templates")
    def seat_templates(_ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        return {"items": store.list_seat_templates()}

    @app.post("/members/invites")
    def create_member_invite(body: dict[str, Any], ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        if not store.has_grant(ctx.principal_id, "org.admin"):
            raise HTTPException(status_code=403, detail="denied")
        return store.create_invite(
            actor_id=ctx.principal_id,
            tenant_id=ctx.tenant_id,
            template=str(body.get("template") or ""),
            label=str(body.get("label") or ""),
        )

    @app.post("/grants")
    def create_grant(body: dict[str, Any], ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        if not store.has_grant(ctx.principal_id, "org.admin"):
            raise HTTPException(status_code=403, detail="denied")
        return store.add_grant(body["principal_id"], body["grant_class"], ctx.tenant_id)

    @app.post("/grants/revoke")
    def revoke_grant(body: dict[str, Any], ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        if not store.has_grant(ctx.principal_id, "org.admin"):
            raise HTTPException(status_code=403, detail="denied")
        return {
            "revoked": store.revoke_grant(body["principal_id"], body["grant_class"]),
            "principal_id": body["principal_id"],
            "grant_class": body["grant_class"],
        }

    @app.post("/entitlements")
    def create_entitlement(body: dict[str, Any], ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        if not store.has_grant(ctx.principal_id, "org.admin"):
            raise HTTPException(status_code=403, detail="denied")
        return store.add_entitlement(body["principal_id"], body["feature"], ctx.tenant_id)

    @app.get("/entitlements/me")
    def my_entitlements(ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        return {"items": store.entitlements(ctx.principal_id)}

    @app.post("/approvals")
    def create_approval(body: dict[str, Any], ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        return store.decide_approval(
            approval_class=body["approval_class"],
            requester_id=body.get("requester_id", ctx.principal_id),
            decider_id=ctx.principal_id,
            target_id=body["target_id"],
            target_version=body.get("target_version", "1"),
            tenant_id=ctx.tenant_id,
        )

    @app.post("/grants/effective")
    def compute_effective(body: dict[str, Any], _ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        grants = effective_grants(
            set(body.get("sponsor", [])),
            set(body.get("toolset", [])),
            set(body.get("mode", [])),
        )
        return {"effective": sorted(grants)}

    @app.post("/priorities")
    def post_priority(body: dict[str, Any], ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        return store.create_priority(ctx.principal_id, body["title"])

    @app.get("/priorities")
    def get_priorities(ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        return {"items": store.list_visible("priorities", ctx.principal_id)}

    @app.post("/plans")
    def post_plan(body: dict[str, Any], ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        return store.create_plan(ctx.principal_id, body["title"], body.get("priority_id"))

    @app.get("/plans")
    def get_plans(ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        return {"items": store.list_visible("plans", ctx.principal_id)}

    @app.post("/work-items")
    def post_work_item(body: dict[str, Any], ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        return store.create_work_item(ctx.principal_id, body["title"], body.get("plan_id"))

    @app.get("/work-items")
    def get_work_items(ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        return {"items": store.list_visible("work_items", ctx.principal_id)}

    @app.get("/work-items/{work_item_id}")
    def get_work_item(work_item_id: str, ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        return store.get_work_item(ctx.principal_id, work_item_id)

    @app.post("/work-items/{work_item_id}/stage")
    def post_work_item_stage(
        work_item_id: str, body: dict[str, Any], ctx: AuthContext = Depends(auth_dep)
    ) -> dict[str, Any]:
        return store.advance_stage(
            ctx.principal_id,
            work_item_id,
            str(body.get("stage") or ""),
            body.get("evidence"),
        )

    @app.post("/assignments")
    def post_assignment(body: dict[str, Any], ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        return store.create_assignment(ctx.principal_id, body["work_item_id"], body["principal_id"])

    @app.post("/dependencies")
    def post_dependency(body: dict[str, Any], ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        return store.create_dependency(ctx.principal_id, body["from_work_item_id"], body["to_work_item_id"])

    @app.post("/source-references")
    def post_source_ref(body: dict[str, Any], ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        return store.create_source_reference(
            ctx.principal_id, body["provider"], body["installation_pointer"]
        )

    @app.get("/records")
    def records(ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        return {"items": store.list_records(ctx.principal_id)}

    @app.get("/search")
    def search(q: str = "", ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        return {"items": store.search(ctx.principal_id, q)}

    @app.get("/aggregates")
    def aggregates(ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        return store.aggregates(ctx.principal_id)

    @app.post("/attachments")
    def post_attachment(body: dict[str, Any], ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        att = store.create_attachment(ctx.principal_id, body.get("label", "file"))
        expires = int(time.time()) + SIGNED_URL_TTL
        sig = _sign(settings.attachment_signing_key, att["id"], expires)
        return {
            **att,
            "signed_url": f"/attachments/{att['id']}?expires={expires}&sig={sig}",
            "ttl_seconds": SIGNED_URL_TTL,
        }

    @app.get("/attachments/{attachment_id}")
    def get_attachment(
        attachment_id: str,
        expires: int = Query(...),
        sig: str = Query(...),
        ctx: AuthContext = Depends(auth_dep),
    ) -> dict[str, Any]:
        store.require_surface(ctx.principal_id, "attachments")
        if int(time.time()) > expires:
            raise HTTPException(status_code=403, detail="signed url expired")
        expected = _sign(settings.attachment_signing_key, attachment_id, expires)
        if not hmac.compare_digest(expected, sig):
            raise HTTPException(status_code=403, detail="signed url invalid")
        if expires - int(time.time()) > SIGNED_URL_TTL:
            raise HTTPException(status_code=403, detail="signed url ttl exceeds 300s")
        return store.get_attachment(attachment_id)

    @app.get("/notifications")
    def notifications(ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        return {"items": store.list_notifications(ctx.principal_id)}

    @app.get("/memory")
    def memory(ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        return {"items": store.list_memory(ctx.principal_id)}

    @app.post("/jobs")
    def post_job(body: dict[str, Any], ctx: AuthContext = Depends(auth_dep)) -> JSONResponse:
        job = store.persist_job(ctx.principal_id, body.get("purpose", "dev.long_step"))
        # persist-before-202: job is on disk before this response is built
        if settings.test_hooks and os.environ.get("ENGINE_TEST_CRASH_AFTER_PERSIST") == "1":
            raise RuntimeError("crash after persist")
        store.start_job(job["id"], ctx.principal_id)
        if body.get("purpose", "dev.long_step") == "dev.long_step":
            store.add_receipt(job["id"], "long_step", body.get("idempotency_key") or f"{job['id']}:long_step")
            store.complete_job(job["id"])
        refreshed = store.get_job(job["id"])
        return JSONResponse(refreshed, status_code=202)

    @app.get("/jobs/{job_id}")
    def get_job(job_id: str, ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        if not store.has_grant(ctx.principal_id, "run.start") and not store.has_grant(
            ctx.principal_id, "org.admin"
        ):
            raise HTTPException(status_code=403, detail="denied")
        return store.get_job(job_id)

    @app.post("/jobs/{job_id}/cancel")
    def cancel_job(job_id: str, ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        return store.cancel_job(ctx.principal_id, job_id)

    @app.post("/jobs/{job_id}/steps")
    def job_step(job_id: str, body: dict[str, Any], ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        if not store.has_grant(ctx.principal_id, "run.start") and not store.has_grant(
            ctx.principal_id, "org.admin"
        ):
            raise HTTPException(status_code=403, detail="denied")
        if body.get("target_id"):
            store.require_live_approval(str(body["target_id"]), str(body.get("target_version") or "1"))
            store.void_approval_if_changed(str(body["target_id"]), str(body.get("target_version") or "1"))
        return store.add_receipt(job_id, body["step_name"], body["idempotency_key"])

    @app.get("/jobs/{job_id}/events")
    def job_events(
        job_id: str,
        last_event_id: int = Query(default=0),
        ctx: AuthContext = Depends(auth_dep),
    ) -> StreamingResponse:
        if not store.has_grant(ctx.principal_id, "run.start") and not store.has_grant(
            ctx.principal_id, "org.admin"
        ):
            raise HTTPException(status_code=403, detail="denied")
        events = store.events_after(job_id, last_event_id)

        def stream() -> Any:
            for event in events:
                data = json.dumps({"type": event["type"], "payload": event["payload"]})
                yield f"id: {event['id']}\nevent: {event['type']}\ndata: {data}\n\n"
            # disconnect ≠ cancel: stream ends; job status unchanged

        return StreamingResponse(stream(), media_type="text/event-stream")

    @app.post("/usage")
    def post_usage(body: dict[str, Any], ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        validate_usage_event(body)
        inserted = emit_usage(store, settings.usage_emit, body)
        return {"emitted": inserted is not None, "id": inserted}

    @app.get("/usage/count")
    def usage_count(ctx: AuthContext = Depends(auth_dep)) -> dict[str, int]:
        if not store.has_grant(ctx.principal_id, "usage.read") and not store.has_grant(
            ctx.principal_id, "org.admin"
        ):
            raise HTTPException(status_code=403, detail="denied")
        return {"count": store.usage_count()}

    @app.post("/admin/destructive")
    def destructive(ctx: AuthContext = Depends(auth_dep)) -> dict[str, str]:
        require_reauth(ctx)
        return {"status": "ok"}

    @app.get("/github/pulls")
    def github_list_pulls(ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        return list_pulls(
            settings.github_app_id,
            settings.github_installation_id,
            settings.github_private_key_path,
            owner=settings.github_owner,
            repo=settings.github_repo,
        )

    @app.get("/github/grants")
    def github_grant_intersection(ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        orgos = {
            row["grant_class"]
            for row in store.conn.execute(
                "SELECT grant_class FROM grants WHERE principal_id=?",
                (ctx.principal_id,),
            ).fetchall()
        }
        perms = installation_permissions(
            settings.github_app_id,
            settings.github_installation_id,
            settings.github_private_key_path,
        )
        effective = sorted(intersect_repo_grants(orgos, perms))
        return {
            "orgos": sorted(g for g in orgos if g.startswith("repo.")),
            "installation": perms,
            "effective": effective,
        }

    @app.post("/assistant/sessions")
    def create_assistant_session(body: dict[str, Any], ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        return store.create_conversation(ctx.principal_id, str(body.get("title") or "Hey Engine"), str(body.get("mode") or "Ask"))

    @app.get("/assistant/sessions")
    def list_assistant_sessions(ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        return {"items": store.list_conversations(ctx.principal_id)}

    @app.get("/assistant/sessions/{session_id}")
    def get_assistant_session(session_id: str, ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        return {
            "id": session_id,
            "messages": store.list_messages(ctx.principal_id, session_id),
        }

    @app.post("/assistant/sessions/{session_id}/turns")
    def post_assistant_turn(
        session_id: str, body: dict[str, Any], ctx: AuthContext = Depends(auth_dep)
    ) -> dict[str, Any]:
        text = str(body.get("content") or "").strip()
        if not text:
            raise HTTPException(status_code=400, detail="content is required")
        user_msg = store.add_message(ctx.principal_id, session_id, "user", text)
        job = store.persist_job(ctx.principal_id, "assistant.turn")
        hermes = probe_hermes(settings.hermes_api_base_url)
        if hermes != "reachable":
            assistant = store.add_message(
                ctx.principal_id,
                session_id,
                "system",
                "Hermes API server is not reachable. Your message is saved. Closing this panel will not discard it.",
            )
            store.add_receipt(job["id"], "assistant.blocked_runtime", f"{job['id']}:blocked")
            runtime = {"status": "blocked_runtime", "hermes": hermes}
        else:
            assistant = store.add_message(
                ctx.principal_id,
                session_id,
                "system",
                "Message saved. The worker starts a Hermes run when the API server (not the login UI) is listening.",
            )
            store.add_receipt(job["id"], "assistant.queued", f"{job['id']}:queued")
            runtime = {"status": "queued", "hermes": hermes}
        return {"user": user_msg, "reply": assistant, "job": job, "runtime": runtime}

    @app.post("/runs")
    def post_run(body: dict[str, Any], ctx: AuthContext = Depends(auth_dep)) -> JSONResponse:
        job = store.persist_job(ctx.principal_id, str(body.get("purpose") or "run"))
        store.add_receipt(job["id"], "run.persist", str(body.get("idempotency_key") or f"{job['id']}:start"))
        hermes = probe_hermes(settings.hermes_api_base_url)
        runtime = {
            "status": "queued" if hermes == "reachable" else "blocked_runtime",
            "hermes": hermes,
        }
        return JSONResponse({"job": job, "runtime": runtime}, status_code=202)

    @app.post("/github/pulls")
    def github_open_pull(body: dict[str, Any], ctx: AuthContext = Depends(auth_dep)) -> dict[str, Any]:
        if not store.has_grant(ctx.principal_id, "org.admin") and not store.has_grant(
            ctx.principal_id, "repo.change"
        ):
            raise HTTPException(status_code=403, detail="denied")
        dry_run = body.get("dry_run", True)
        if dry_run is False or dry_run == "false":
            require_reauth(ctx)
            dry = False
            configured = bool(
                (settings.github_app_id or "").strip()
                and (settings.github_installation_id or "").strip()
                and (settings.github_private_key_path or "").strip()
            )
            if configured:
                orgos = {
                    row["grant_class"]
                    for row in store.conn.execute(
                        "SELECT grant_class FROM grants WHERE principal_id=?",
                        (ctx.principal_id,),
                    ).fetchall()
                }
                perms = installation_permissions(
                    settings.github_app_id,
                    settings.github_installation_id,
                    settings.github_private_key_path,
                )
                if not perms:
                    raise HTTPException(
                        status_code=403,
                        detail="installation permissions are empty; refuse live open",
                    )
                if not may_open_pull(orgos, perms):
                    raise HTTPException(
                        status_code=403,
                        detail="repo.change is not in the installation intersection",
                    )
        else:
            dry = True
        result = open_pull(
            settings.github_app_id,
            settings.github_installation_id,
            settings.github_private_key_path,
            owner=str(body.get("owner") or settings.github_owner),
            repo=str(body.get("repo") or settings.github_repo),
            title=str(body.get("title") or ""),
            body=str(body.get("body") or ""),
            head=str(body.get("head") or ""),
            base=str(body.get("base") or "main"),
            dry_run=dry,
        )
        store.append_audit(
            ctx.principal_id,
            "github.pull.plan" if dry else "github.pull.open",
            "repo",
            f"{result.get('planned', {}).get('owner', '')}/{result.get('planned', {}).get('repo', '')}",
        )
        return result

    return app


def _sign(key: str, attachment_id: str, expires: int) -> str:
    return hmac.new(
        key.encode(), f"{attachment_id}:{expires}".encode(), hashlib.sha256
    ).hexdigest()


app = create_app()
