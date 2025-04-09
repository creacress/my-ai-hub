from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.core.security import verify_token
from app.core.config import OLLAMA_URL
import httpx

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str
    model: str = "llama3"  # modèle par défaut

@router.post("/ask")
async def ask(data: PromptRequest, user=Depends(verify_token)):
    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                f"{OLLAMA_URL}/api/generate",
                json={
                    "prompt": data.prompt,
                    "model": data.model,
                    "stream": False
                }
            )
            response.raise_for_status()
            try:
                result = response.json()
                return {"response": result.get("response", "").strip()}
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Invalid JSON response: {e}")
    except httpx.HTTPStatusError as http_err:
        raise HTTPException(status_code=http_err.response.status_code, detail=http_err.response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
