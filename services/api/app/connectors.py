"""B12 connector catalogue. Deny-by-default. No secrets in this module."""

from __future__ import annotations

from typing import Any

# Destination class is recorded before enablement (DRR-04, LIC-20).
CONNECTORS: dict[str, dict[str, Any]] = {
    "github": {
        "id": "github",
        "label": "GitHub",
        "kind": "Bound repository",
        "destination_class": "source_control",
        "status": "configured",
        "actions": {"read": True, "write": "dry_run_or_approval", "send": False},
        "handoff": "Authorise the GitHub App in the browser. Papership never embeds a provider sign-in.",
    },
    "gmail": {
        "id": "gmail",
        "label": "Gmail",
        "kind": "Comms channel",
        "destination_class": "mailbox",
        "status": "planned",
        "actions": {"read": "dry_run", "draft": "dry_run", "send": "approval_then_receipt"},
        "handoff": "Create a Google OAuth client, then set GMAIL_OAUTH_CLIENT_ID and GMAIL_OAUTH_REDIRECT_URL. Send stays approval-bound.",
    },
    "slack": {
        "id": "slack",
        "label": "Slack",
        "kind": "Comms channel",
        "destination_class": "chat",
        "status": "planned",
        "actions": {"read": "dry_run", "send": "approval_then_receipt"},
        "handoff": "Create a Slack app, then set SLACK_CLIENT_ID. Messages stay approval-bound.",
    },
    "telegram": {
        "id": "telegram",
        "label": "Telegram",
        "kind": "Comms channel",
        "destination_class": "chat",
        "status": "planned",
        "actions": {"read": False, "send": "approval_then_receipt"},
        "handoff": "Telegram stays planned until a bot mapping is supplied.",
    },
    "whatsapp": {
        "id": "whatsapp",
        "label": "WhatsApp",
        "kind": "Comms channel",
        "destination_class": "chat",
        "status": "planned",
        "actions": {"read": False, "send": "approval_then_receipt"},
        "handoff": "WhatsApp Cloud API stays planned until a business mapping is supplied.",
    },
}


def list_connectors() -> list[dict[str, Any]]:
    return [dict(row) for row in CONNECTORS.values()]


def get_connector(provider: str) -> dict[str, Any] | None:
    return CONNECTORS.get((provider or "").strip().lower())
