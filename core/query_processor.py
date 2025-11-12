# from client.server_client import client
from client.llm_client import openAi_client
import json
import os
from dotenv import load_dotenv

load_dotenv()

ngrok_url = os.getenv("NGROK_URL")


async def process_query(query: str) -> str:
    """Process a query using a connected LLM
    and available
    tools from your server"""
    response = openAi_client.responses.create(
        model="openai/gpt-oss-120b",
        tools=[
            {
                "type": "mcp",
                "server_label": "meducate_server",
                # pass your server url here, for openAI llm it should be ngrok
                # or a hosted server, localhost doesnt seem to work...
                "server_url": f"{ngrok_url}/mcp",
                "require_approval": "never",
            }  # noqa
        ],  # noqa
        input=query,
    )
    result = {
        "status": response.status,
        "model": response.model,
        "message": None,
        "reasoning": None,
        "tool_calls": [],
        "usage": {
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens,
            "reasoning_tokens": response.usage.output_tokens_details.reasoning_tokens,  # noqa
            "total_tokens": response.usage.total_tokens,
        },
    }

    # Extract meaningful information from output
    for item in response.output:
        if item.type == "reasoning":
            if item.content:
                result["reasoning"] = item.content[0].text

        elif item.type == "mcp_call":
            # Extract tool call details
            result["tool_calls"].append(
                {
                    "tool": item.name,
                    "arguments": json.loads(item.arguments),
                    "output": item.output,
                    "status": item.status,
                }
            )

        elif item.type == "message":
            # Extract final message
            result["message"] = item.content[0].text

    return result
