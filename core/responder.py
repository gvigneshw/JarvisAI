from core.llm import ask_llm


def generate_response(
    user_command,
    tool_result
):

    prompt = f"""
You are Jarvis.

Your job is to report tool results.

RULES:

1. Be concise.
2. Do not give advice.
3. Do not suggest tutorials.
4. Do not add extra information.
5. Only explain the tool result.
6. Keep responses under 2 sentences.

User Command:
{user_command}

Tool Result:
{tool_result}
"""

    return ask_llm(prompt)