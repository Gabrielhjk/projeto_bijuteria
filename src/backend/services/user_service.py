from backend.dto.user.user_update_dto import UserUpdateDto
from backend.dto.user.user_request_dto import UserRequestDto
from backend.models import Users
from sqlalchemy.orm import Session
from fastapi import HTTPException
from argon2 import PasswordHasher
from sqlalchemy import select

def get_all_users(session: Session):
    users_query = select(Users)
    users = session.scalars(users_query).all()
    return users

def get_user_id(id: int, session: Session):
    user = session.get(Users, id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuário näo Existe!")

    return user

def created_user(body: UserRequestDto, session: Session):
    ph = PasswordHasher()
    hash = ph.hash(body.password)

    user = Users(
        name=body.name,
        phone=body.phone,
        login=body.login,
        password=hash,
        type_user=body.type_user,
        obs=body.obs
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    return user

def updated_user(id: int, body: UserUpdateDto, session: Session):
    ph = PasswordHasher()
    user = session.get(Users, id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuário não Encontrado!")

    user.name = body.name
    user.phone = body.phone
    user.login = body.login
    user.type_user = body.type_user
    user.obs = body.obs
    user.active = body.active

    if body.password:
        user.password = ph.hash(body.password)
    
    session.commit()
    session.refresh(user)   

    return user 

def delete_user(id: int, session: Session):
    user = session.get(Users, id)
    if user is None:
       raise HTTPException(status_code=404, detail="Usuário não encontrado!")

    session.delete(user)