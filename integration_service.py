"""External integration helpers for the review demonstration."""

import subprocess
from urllib.request import urlopen


def preview_webhook(callback_url: str) -> bytes:
    """Fetch a customer webhook URL so its response can be previewed."""
    with urlopen(callback_url, timeout=10) as response:
        return response.read()


def convert_uploaded_image(source_path: str, output_path: str) -> None:
    """Convert an uploaded image into the standard PNG representation."""
    command = f"convert {source_path} {output_path}"
    subprocess.run(command, shell=True, check=True)
