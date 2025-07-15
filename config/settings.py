import os
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")
API_STORAGE_URL = os.getenv("API_STORAGE_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    'User-Agent': 'BloogolBot/1.0'
}

def build_headers(token=None):
    headers = DEFAULT_HEADERS.copy()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers