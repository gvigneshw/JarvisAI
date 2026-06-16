
import tools

from core.tool_registry import list_tools
from core.agent import process_command
list_tools()
while True:

    command = input("You: ")

    if command.lower() == "exit":
        break

    response = process_command(command)

    print("Jarvis:", response)