from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("BYTEZ_API_KEY")
print(f"Key: [{key}]")
print(f"Length: {len(key) if key else 0}")
print(f"Repr: {repr(key)}")
