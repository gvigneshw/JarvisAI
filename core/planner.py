import json
from urllib import response

from core.json_parser import parse_json
from core.llm import ask_llm
from core.tool_registry import get_available_tools


EXAMPLES = """
Examples:

User: open notepad
{{"tool":"open_app","app":"notepad"}}

User: open calculator
{{"tool":"open_app","app":"calculator"}}

User: open paint
{{"tool":"open_app","app":"paint"}}


User: search python decorators
{{"tool":"browser_search","query":"python decorators"}}

User: search best gaming laptop under 50000
{{"tool":"browser_search","query":"best gaming laptop under 50000"}}

(For browser searches, preserve the user's search text exactly.)


User: create file notes.txt
{{"tool":"create_file","filename":"notes.txt"}}

User: create file todo.txt
{{"tool":"create_file","filename":"todo.txt"}}

User: make a file called report.txt
{{"tool":"create_file","filename":"report.txt"}}

(When creating files:

Use the filename exactly as provided.)

User: read notes.txt
{{"tool":"read_file","filename":"notes.txt"}}

User: open todo.txt
{{"tool":"read_file","filename":"todo.txt"}}

User: show report.txt
{{"tool":"read_file","filename":"report.txt"}}


User: write hello world to notes.txt
{{"tool":"write_file","filename":"notes.txt","content":"hello world"}}

User: write python is awesome to notes.txt
{{"tool":"write_file","filename":"notes.txt","content":"python is awesome"}}

User: save buy milk in todo.txt
{{"tool":"write_file","filename":"todo.txt","content":"buy milk"}}

(When using write_file:

Extract:
- filename
- content

Preserve the content exactly.)


User: append buy eggs to todo.txt
{{"tool":"append_file","filename":"todo.txt","content":"buy eggs"}}

User: append today i learned python to notes.txt
{{"tool":"append_file","filename":"notes.txt","content":"today i learned python"}}

User: add milk to shopping.txt
{{"tool":"append_file","filename":"shopping.txt","content":"milk"}}

(When the user wants to add text to an existing file,
use append_file.)


User: list files
{{"tool":"list_files"}}

User: show files
{{"tool":"list_files"}}

User: what files do I have
{{"tool":"list_files"}}


User: delete notes.txt
{{"tool":"delete_file","filename":"notes.txt"}}

User: remove todo.txt
{{"tool":"delete_file","filename":"todo.txt"}}



User: open notes.txt
{{"tool":"open_file","filename":"notes.txt"}}

User: open report.txt
{{"tool":"open_file","filename":"report.txt"}}

User: open todo.txt
{{"tool":"open_file","filename":"todo.txt"}}

(If the user mentions a filename with an extension
(.txt, .pdf, .docx, etc.)

use open_file.

If the user mentions an application
(calculator, notepad, paint, chrome)

use open_app.)


User: what time is it
{{"tool":"get_time"}}

User: tell me the time
{{"tool":"get_time"}}

User: current time
{{"tool":"get_time"}}


User: what date is it
{{"tool":"get_date"}}

User: today's date
{{"tool":"get_date"}}

User: current date
{{"tool":"get_date"}}



If no suitable tool exists:

{{"tool":"none"}}

"""

def plan_action(user_command):

    tools = get_available_tools()

    tool_text = ""

    for name, data in tools.items():
        tool_text += f"""
Tool Name: {name}

Description:
{data['description']}

Parameters:
{data['parameters']}
"""

    prompt = f"""
You are Jarvis.

You are a tool routing AI.

AVAILABLE TOOLS:

{tool_text}

RULES:

1. Return ONLY valid JSON
2. No explanations
3. No markdown
4. No code blocks
5. Use ONLY tool names listed above
6. Never invent tool names


{EXAMPLES}

User Command:
{user_command}
"""

    response = ask_llm(prompt)

    print("\n--- RAW MODEL OUTPUT ---")
    print(response)
    print("------------------------\n")

    from core.json_parser import parse_json

    action = parse_json(response)

    if action is None:
        print("JSON PARSE FAILED")
        return None

    return action