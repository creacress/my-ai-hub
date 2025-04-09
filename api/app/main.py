from fastapi import FastAPI
from app.routes import ollama

app = FastAPI(title="AI Hub")

app.include_router(ollama.router, prefix="/ollama")
