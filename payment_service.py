"""Checkout operations for the review demonstration."""

import sqlite3
from typing import Protocol


class PaymentGateway(Protocol):
    def charge(self, user_id: int, amount_cents: int) -> str: ...


def checkout(
    gateway: PaymentGateway,
    connection: sqlite3.Connection,
    user_id: int,
    amount_cents: int,
) -> dict[str, str]:
    """Charge a user and record the completed order."""
    receipt_id = gateway.charge(user_id, amount_cents)

    connection.execute(
        "INSERT INTO orders (user_id, amount_cents, receipt_id) VALUES (?, ?, ?)",
        (user_id, amount_cents, receipt_id),
    )
    connection.commit()

    return {"status": "paid", "receipt_id": receipt_id}
