def convert_mcp_to_groq(mcp_tools):
    groq_tools = []
    for tools in mcp_tools:
        groq_tools.append(
            {
                "type": "function",
                "function": {
                    "name": tools.name,
                    "description": tools.description,
                    "parameters": tools.inputSchema,
                },
            }
        )
        return groq_tools
