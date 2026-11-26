from app.security.jwt import create_access_token
from app.db.models.user import User
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi import HTTPException
from argon2 import PasswordHasher
from sqlalchemy import select

def login_service(form_data: OAuth2PasswordRequestForm, session: Session):
    # faz a query  
    user_query = select(User).where(User.login == form_data.username)

    # executa a query
    user = session.scalars(user_query).first()

    if user is None:
        raise HTTPException(status_code=404, detail="Usuário Inválido")

    # chamando a classe de criptografia do argon2
    ph = PasswordHasher()

    try:
        # verifica se a senha criptografada é a mesma senha que foi digitada
        ph.verify(user.password, form_data.password)
    except:
        raise HTTPException(status_code=404, detail="Senha Inválida")

    # payload para o token criado apos o login do usuario
    payload = {
        "sub": str(user.id),
        "name": user.name,
        "role": user.type_user
    }

    if payload["role"] == "Motorista":
        raise HTTPException(status_code=404, detail="Usuário não é um Administrador")

    # cria o token 
    token = create_access_token(payload)

    return {
        "access_token": token,
        "token_type": "bearer"
    } 