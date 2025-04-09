import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("ENV", "dev")
OLLAMA_URL = os.getenv("OLLAMA_URL_PROD") if ENV == "prod" else os.getenv("OLLAMA_URL_DEV")
