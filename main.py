from client.server_client import client
import asyncio
from core.query_processor import process_query
import json


async def main():
    print("Hello from meducate_client!")
    async with client:
        await client.ping()
        # tools = await client.list_tools()
        # print(tools)
        result = await process_query(
            "send an email to obliepius14@gmail.com and tell him to buy water on his way home"  # noqa
        )
        print("-" * 60)
        print("📥 RESPONSE")
        print("-" * 60)
        print(f"\n{json.dumps(result, indent=2)}\n")
        print("=" * 60 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
