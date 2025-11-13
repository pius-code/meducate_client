from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_KEY = os.getenv("GROQ_API_KEY")
BYTEZ_KEY = os.getenv("BYTEZ_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_AI_TOKEN")

openAi_client = OpenAI(
    api_key=GROQ_KEY, base_url="https://api.groq.com/openai/v1"
)  # noqa

# Initialize Bytez OpenAI client, get key from bytez.com/api....
#  gives you access to some premium models like gpt5...
# sadly doesnt support mcp yet. but it works
openAi_client2 = OpenAI(
    api_key=BYTEZ_KEY,
    base_url="https://api.bytez.com/models/v2/openai/v1",
    default_headers={"Authorization": BYTEZ_KEY},
)

openAi_client3 = OpenAI(
    api_key=GITHUB_TOKEN,
    base_url="https://models.github.ai/inference",
)
