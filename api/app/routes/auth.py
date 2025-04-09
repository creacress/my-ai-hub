from fastapi import APIRouter, Form, HTTPException, status
from app.core.security import create_access_token, verify_password
from pathlib import Path
import json
from datetime import timedelta

router = APIRouter()
USERS_FILE = Path(__file__).parent.parent / "users.json"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def get_user(username: str):
    if not USERS_FILE.exists():
        return None
    with USERS_FILE.open() as f:
        users = json.load(f)
        return next((u for u in users if u["username"] == username), None)

@router.post("/token")
async def login(username: str = Form(...), password: str = Form(...)):
    user = get_user(username)
    if not user or not verify_password(password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Nom d'utilisateur ou mot de passe incorrect",
        )

    access_token = create_access_token(
        data={"sub": username},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    return {"access_token": access_token, "token_type": "bearer"}
