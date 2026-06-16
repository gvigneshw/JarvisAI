from pathlib import Path

from core.tool_registry import register_tool


def read_file(filename):

    file_path = Path(filename)

    if not file_path.exists():
        return f"File not found: {filename}"

    try:

        content = file_path.read_text(
            encoding="utf-8"
        )

        return content

    except Exception as e:

        return f"Error reading file: {e}"


register_tool(
    "read_file",
    "Read a text file",
    read_file,
    parameters={
        "filename": "string"
    }
)