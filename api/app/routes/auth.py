from fastapi import APIRouter, Form, HTTPException
from app.core.security import create_access_token

router = APIRouter()

@router.post("/token")
async def login(username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "password":  # 💡 à sécuriser plus tard
        access_token = create_access_token(data={"sub": username})
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Bad credentials")
