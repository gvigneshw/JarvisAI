# from pathlib import Path

# from core.tool_registry import register_tool


# def delete_file(filename):

#     file_path = Path(filename)

#     if not file_path.exists():
#         return f"File not found: {filename}"

#     file_path.unlink()

#     return f"Deleted {filename}"


# register_tool(
#     "delete_file",
#     "Delete a file",
#     delete_file,
#     parameters={
#         "filename": "string"
#     }
# )