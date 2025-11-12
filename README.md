# Meducate Client

A Python client for interacting with the Meducate MCP (Model Context Protocol) server using Groq's inference API with OpenAI SDK compatibility. This client enables AI-powered medical education assistance through intelligent tool calling and query processing.

## 🌟 Features

- **Groq-Powered LLM Integration**: Uses Groq's fast inference API with OpenAI SDK
- **MCP Tool Support**: Seamlessly connects to Meducate MCP server for medical education tools
- **Async/Await Architecture**: Built with modern asynchronous Python patterns
- **Flexible Model Support**: Compatible with multiple LLM models optimized for tool calling
- **Query Processing**: Intelligent query routing with reasoning and tool call tracking

## 🤖 Supported Models

The client supports the following Groq models with tool calling capabilities:

- `llama-3.1-8b-instant` - Fast Llama 3.1 8B model
- `meta-llama/llama-4-scout-17b-16e-instruct` - Advanced Llama 4 Scout model
- `openai/gpt-oss-120b` - Large-scale open-source GPT model (default)
- `openai/gpt-oss-20b` - Smaller open-source GPT variant

> **Note**: All models are accessed via Groq's inference API using the OpenAI SDK for compatibility.

## 📋 Prerequisites

- Python 3.13 or higher
- Groq API key
- Access to Meducate MCP server (via ngrok or hosted endpoint)

## 🚀 Installation

1. **Clone the repository**:

```bash
git clone <repository-url>
cd meducate_client
```

2. **Install dependencies**:

```bash
pip install -e .
```

Or using uv:

```bash
uv pip install -e .
```

3. **Set up environment variables**:

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
SERVER_URL=https://your-mcp-server-url.ngrok-free.app/mcp
```

## 📁 Project Structure

```
meducate_client/
├── client/
│   ├── llm_client.py       # Groq/OpenAI client configuration
│   └── server_client.py    # MCP server connection
├── core/
│   └── query_processor.py  # Query processing and LLM orchestration
├── utils/
│   └── mcp_to_groq.py      # MCP to Groq tool conversion utilities
├── main.py                 # Main application entry point
├── test_client.py          # Testing utilities
├── pyproject.toml          # Project dependencies
└── README.md               # This file
```

## 💻 Usage

### Basic Usage

```python
from core.query_processor import process_query
import asyncio
import json

async def main():
    result = await process_query(
        "Send an email to user@example.com about medical study resources"
    )
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    asyncio.run(main())
```

### Running the Example

```bash
python main.py
```

### Response Structure

The `process_query` function returns a structured response:

```json
{
  "status": "completed",
  "model": "openai/gpt-oss-120b",
  "message": "Assistant's response message",
  "reasoning": "Model's reasoning process",
  "tool_calls": [
    {
      "tool": "tool_name",
      "arguments": {...},
      "output": "Tool execution result",
      "status": "success"
    }
  ],
  "usage": {
    "input_tokens": 150,
    "output_tokens": 200,
    "reasoning_tokens": 50,
    "total_tokens": 350
  }
}
```

## 🔧 Configuration

### Changing the Model

Edit `core/query_processor.py` to change the model:

```python
response = openAi_client.responses.create(
    model="llama-3.1-8b-instant",  # Change to your preferred model
    # ... rest of configuration
)
```

### Updating MCP Server URL

Update the server URL in `client/server_client.py` or use the `SERVER_URL` environment variable:

```python
client = Client("https://your-new-server-url.ngrok-free.app/mcp")
```

## 🛠️ Development

### Running Tests

```bash
python test_client.py
```

### MCP Tool Conversion

The `utils/mcp_to_groq.py` utility converts MCP tool definitions to Groq-compatible format:

```python
from utils.mcp_to_groq import convert_mcp_to_groq

groq_tools = convert_mcp_to_groq(mcp_tools)
```

## 🔐 Authentication

For OAuth-protected MCP servers, modify the client initialization:

```python
async with Client("http://localhost:8000/mcp", auth="oauth") as client:
    result = await client.call_tool("protected_tool")
```

## 📦 Dependencies

- `fastmcp>=2.13.0.2` - MCP client library
- `openai>=2.7.2` - OpenAI SDK (used with Groq)
- `python-dotenv>=1.2.1` - Environment variable management

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

[Add your license information here]

## 🔗 Related Projects

- [Meducate MCP Server](link-to-server-repo) - The backend MCP server for medical education tools

## 📞 Support

For issues, questions, or contributions, please open an issue on GitHub.

---

**Built with ❤️ for medical students and young doctors**
