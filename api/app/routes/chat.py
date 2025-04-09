from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.core.security import verify_token
from app.core.config import OLLAMA_URL
from app.core.context import SITE_CONTEXT
import httpx

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    model: str = "llama3"

@router.post("/chat")
async def chat(data: ChatRequest, user=Depends(verify_token)):
    prompt = f"{SITE_CONTEXT}\n\nUtilisateur : {data.message}\nAssistant :"

    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                f"{OLLAMA_URL}/api/generate",
                json={"prompt": prompt, "model": data.model, "stream": False}
            )
            response.raise_for_status()
            result = response.json()
            return {"response": result.get("response", "").strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
