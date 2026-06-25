from pathlib import Path

from core.tool_registry import register_tool


def list_files():

    current_directory = Path(".")

    files = []

    for item in current_directory.iterdir():

        if item.is_file():

            files.append(item.name)

    if not files:

        return "No files found."

    return "\n".join(files)


register_tool(
    "list_files",
    "List files in the current directory",
    list_files,
    parameters={}
)