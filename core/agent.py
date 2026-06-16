from core.planner import plan_action
from core.tool_registry import execute_tool
from core.validator import validate_action

def process_command(command):

    action = plan_action(command)

    if not action:
        return "Could not understand command."

    tool_name = action.get("tool")

    if not tool_name:
        return "No tool selected."

    if tool_name == "none":
        return "I don't have a tool for that yet."

    arguments = dict(action)

    arguments.pop("tool", None)
    valid, message = validate_action(action)

    if not valid:
        return message

    return execute_tool(
        tool_name,
        **arguments
    )
   