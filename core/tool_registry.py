# core/tool_registry.py

TOOLS = {}


def register_tool(
    name,
    description,
    function,
    parameters=None
):
    """
    Register a tool.

    Example:

    register_tool(
        "browser_search",
        "Search the web",
        browser_search,
        parameters={
            "query": "string"
        }
    )
    """

    if parameters is None:
        parameters = {}

    TOOLS[name] = {
        "description": description,
        "function": function,
        "parameters": parameters
    }


def execute_tool(name, **kwargs):
    """
    Execute a registered tool.
    """

    if name not in TOOLS:
        return f"Tool '{name}' not found."

    try:
        return TOOLS[name]["function"](**kwargs)

    except Exception as e:
        return f"Error executing tool '{name}': {e}"


def get_available_tools():
    """
    Return all registered tools.
    """

    return TOOLS


def list_tools():
    """
    Debug helper.
    """

    print("\n=== REGISTERED TOOLS ===")

    for name, data in TOOLS.items():

        print(f"\n{name}")

        print("Description:")
        print(data["description"])

        print("Parameters:")
        print(data["parameters"])

    print("\n========================")