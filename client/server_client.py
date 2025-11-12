from fastmcp import Client
import os
from dotenv import load_dotenv

load_dotenv()

ngrok_url = os.getenv("NGROK_URL")

client = Client(f"{ngrok_url}/mcp")
