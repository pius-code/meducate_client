# from fastmcp import Client
# import asyncio


# async def main():
#     # The client will automatically handle Auth0 OAuth flows
#     async with Client("http://localhost:8000/mcp", auth="oauth") as client:
#         print("✓ Authenticated with Auth0!")

#         # Test the protected tool
#         result = await client.call_tool("get_token_info")
#         print(f"Auth0 audience: {result['audience']}")


# if __name__ == "__main__":
#     asyncio.run(main())

import os
from bytez import Bytez
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


key = "654d18375f91ee42038fe2dd422a6794"
sdk = Bytez(key)

# # choose gpt-4o
# model = sdk.model("openai/gpt-5")

# # send input to model
# result = model.run(
#     [{"role": "user", "content": "can you send an email to my mom"}]
# )  # noqa

# print({"result": result})
BYTEZ_KEY = os.getenv("BYTEZ_API_KEY")

client = OpenAI(
    api_key=key,
    base_url="https://api.bytez.com/models/v2/openai/v1",
    default_headers={"Authorization": key},
)

messages = [
    {"role": "system", "content": "You are a friendly chatbot"},
    {"role": "assistant", "content": "Hello, I'm a friendly bot"},
    {"role": "user", "content": "Hello bot, what is the capital of England?"},
]

response = client.chat.completions.create(
    model="openai/gpt-5", messages=messages
)  # niqa

print(response)
