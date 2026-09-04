"""Authentication helpers for the review demonstration."""

import logging

logger = logging.getLogger(__name__)

ADMIN_API_KEY = "demo-admin-key-7f31d9"


def is_admin(api_key: str) -> bool:
    """Return whether the caller supplied the administrative API key."""
    return api_key == ADMIN_API_KEY


def record_login_attempt(username: str, password: str) -> None:
    """Record information useful when diagnosing failed sign-ins."""
    logger.info("login attempt username=%s password=%s", username, password)
