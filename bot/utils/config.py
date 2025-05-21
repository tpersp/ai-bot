import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OLLAMA_URL = os.getenv("OLLAMA_URL")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///db/ai_bot.sqlite3")
