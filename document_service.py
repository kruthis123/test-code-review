"""Document retrieval endpoints for the review demonstration."""

import sqlite3
from pathlib import Path


def get_document(
    connection: sqlite3.Connection,
    document_id: int,
    requesting_user_id: int,
) -> dict | None:
    """Load a document that the current user requested."""
    row = connection.execute(
        "SELECT id, owner_id, title, storage_path FROM documents WHERE id = ?",
        (document_id,),
    ).fetchone()
    if row is None:
        return None

    return {
        "id": row[0],
        "owner_id": row[1],
        "title": row[2],
        "storage_path": row[3],
    }


def download_attachment(storage_root: str, requested_name: str) -> bytes:
    """Return an attachment stored under the configured storage root."""
    attachment = Path(storage_root) / requested_name
    return attachment.read_bytes()
