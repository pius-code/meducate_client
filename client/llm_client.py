from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_KEY = os.getenv("GROQ_API_KEY")

openAi_client = OpenAI(
    api_key=GROQ_KEY, base_url="https://api.groq.com/openai/v1"
)  # noqa
