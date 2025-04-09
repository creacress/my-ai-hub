from fastapi import APIRouter, Request, HTTPException
import httpx

router = APIRouter()

@router.post("/ask")
async def ask(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")

    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                "http://ollama:11434/api/generate",
                json={"prompt": prompt, "model": "llama3"}
            )
            response.raise_for_status()
            return response.json()
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Ollama unreachable: {str(e)}")
