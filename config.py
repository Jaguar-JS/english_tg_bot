import os
from dotenv import load_dotenv

load_dotenv()

TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
OPEN_AI_TOKEN = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not all([TG_BOT_TOKEN, OPEN_AI_TOKEN, GROQ_API_KEY]):
    raise ValueError("Введите токены в .env")