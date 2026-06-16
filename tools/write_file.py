from pathlib import Path

from core.tool_registry import register_tool


def write_file(filename, content):

    filename = filename.strip()

    file_path = Path(filename)

    file_path.write_text(
        content,
        encoding="utf-8"
    )

    return f"Written to {filename}"


register_tool(
    "write_file",
    "Write text to a file. Overwrites existing content.",
    write_file,
    parameters={
        "filename": "string",
        "content": "string"
    }
)