from datetime import datetime

from core.tool_registry import register_tool


def get_date():

    current_date = datetime.now().strftime(
        "%d-%m-%Y"
    )

    return current_date


register_tool(
    "get_date",
    "Get the current date",
    get_date,
    parameters={}
)