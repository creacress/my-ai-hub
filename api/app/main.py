from fastapi import FastAPI
from app.routes import ollama, auth, chat

app = FastAPI(
    title="My AI Hub",
    version="1.0.0",
    description="API centrale pour projets IA + Ollama"
)

# Routes publiques (auth/token)
app.include_router(auth.router, prefix="/auth", tags=["Auth"])

# Routes IA protégées
app.include_router(ollama.router, prefix="/ollama", tags=["Ollama"])
app.include_router(chat.router, prefix="/ai", tags=["Assistant IA"])
