from pathlib import Path

from core.tool_registry import register_tool


def append_file(filename, content):

    filename = filename.strip()

    file_path = Path(filename)

    if not file_path.exists():
        return f"File not found: {filename}"

    with open(
        file_path,
        "a",
        encoding="utf-8"
    ) as file:

        file.write("\n" + content)

    return f"Appended to {filename}"


register_tool(
    "append_file",
    "Append text to an existing file",
    append_file,
    parameters={
        "filename": "string",
        "content": "string"
    }
)