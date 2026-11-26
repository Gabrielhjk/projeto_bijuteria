from backend.security.authentication import get_current_user
from fastapi import HTTPException, Depends
from typing import Annotated

def require_admin(user: Annotated[dict, Depends(get_current_user)]):
    if user["type_user"] != "Administrador":
        raise HTTPException(status_code=403, detail="Acesso Negado")

    return user