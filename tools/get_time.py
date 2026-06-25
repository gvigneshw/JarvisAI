from datetime import datetime

from core.tool_registry import register_tool


def get_time():

    current_time = datetime.now().strftime(
        "%H:%M:%S"
    )

    return current_time


register_tool(
    "get_time",
    "Get the current system time",
    get_time,
    parameters={}
)