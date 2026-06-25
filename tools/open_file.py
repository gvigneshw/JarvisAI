from pathlib import Path
import os

from core.tool_registry import register_tool


def open_file(filename):

    file_path = Path(filename)

    if not file_path.exists():
        return f"File not found: {filename}"

    os.startfile(file_path)

    return f"Opened {filename}"


register_tool(
    "open_file",
    "Open a file using its default application",
    open_file,
    parameters={
        "filename": "string"
    }
)