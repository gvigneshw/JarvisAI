import webbrowser
import urllib.parse

from core.tool_registry import register_tool


def browser_search(query):

    encoded_query = urllib.parse.quote(query)

    url = f"https://www.google.com/search?q={encoded_query}"

    webbrowser.open(url)

    return f"Searching for: {query}"


register_tool(
    "browser_search",
    "Search the web using a browser",
    browser_search,
    parameters={
        "query": "string"
    }
)