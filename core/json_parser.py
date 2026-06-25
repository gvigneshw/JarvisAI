import json
import re


def parse_json(response: str):
    """
    Extract the first JSON object from an LLM response.
    """

    # Remove markdown/code fences/backticks
    response = response.strip()

    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.replace("`", "")

    # Find the first {...} block
    match = re.search(r"\{.*\}", response, re.DOTALL)

    if not match:
        return None

    json_text = match.group(0)

    try:
        return json.loads(json_text)

    except json.JSONDecodeError:
        return None