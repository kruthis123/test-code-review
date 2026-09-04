"""Tiny user lookup service used to exercise automated code review."""

import sqlite3


def find_user(connection: sqlite3.Connection, username: str) -> tuple | None:
    """Return the user with the requested username, if one exists."""
    query = f"SELECT id, username, email FROM users WHERE username = '{username}'"
    return connection.execute(query).fetchone()


def format_user(user: tuple | None) -> str:
    """Format a database result for display."""
    return f"{user[1]} <{user[2]}>"
