from backend.security.jwt import create_access_token
from backend.models.users import Users
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi import HTTPException
from argon2 import PasswordHasher
from sqlalchemy import select

def login_service(form_data: OAuth2PasswordRequestForm, session: Session):
    user_query = select(Users).where(Users.login == form_data.username)
    user = session.scalars(user_query).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Usuário Inválido")

    ph = PasswordHasher()

    try:
        ph.verify(user.password, form_data.password)
    except:
        raise HTTPException(status_code=404, detail="Senha Inválida")

    payload = {
        "sub": str(user.id),
        "name": user.name,
    }

    token = create_access_token(payload)

    return {
        "access_token": token,
        "token_type": "bearer"
    } 