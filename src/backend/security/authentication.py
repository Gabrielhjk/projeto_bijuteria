from backend.security.jwt import decode_access_token
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends
from typing import Annotated

outh2 = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(token: Annotated[str, Depends(outh2)]):
    payload = decode_access_token(token)
    user_id = payload.get("sub")

    if user_id is None:
        raise HTTPException(status_code=401, detail="Credenciais Inválidas")

    return {
        "user_id": user_id,
    }