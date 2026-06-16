from pathlib import Path

from core.tool_registry import register_tool


def create_file(filename):
    filename = filename.strip()

    file_path = Path(filename)

    if file_path.exists():
        return f"File already exists: {filename}"

    file_path.touch()

    return f"Created file: {filename}"


register_tool(
    "create_file",
    "Create a new empty file",
    create_file,
    parameters={
        "filename": "string"
    }
)