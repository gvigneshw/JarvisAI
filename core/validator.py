from core.tool_registry import get_available_tools


def validate_action(action):

    tool_name = action.get("tool")

    tools = get_available_tools()

    if tool_name not in tools:
        return False, "Unknown tool"

    required = tools[tool_name]["parameters"]

    for parameter in required:

        if parameter not in action:

            return (
                False,
                f"Missing parameter: {parameter}"
            )

    return True, "OK"