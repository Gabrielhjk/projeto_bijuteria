from backend.dto.user.user_update_dto import UserUpdateRequestDto
from backend.dto.user.user_response_dto import UserResponseDto
from backend.dto.user.user_request_dto import UserRequestDto
from backend.security.authorization import require_admin
from backend.services.user_service import get_all_users
from backend.services.user_service import get_user_id
from backend.services.user_service import created_user
from backend.services.user_service import updated_user
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from backend.db.db import get_db

router = APIRouter()

@router.get("/", response_model=list[UserResponseDto], status_code=status.HTTP_200_OK)
async def get_users(session: Session = Depends(get_db)):
    users = get_all_users(session)
    return users

@router.get("/{id}", response_model=UserResponseDto, status_code=status.HTTP_200_OK)
async def get_user(id: int, session: Session = Depends(get_db)):
    user = get_user_id(id, session)
    return UserResponseDto.model_validate(user)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(body: UserRequestDto, session: Session = Depends(get_db)):
    created_user(body, session)
    return {"message": "Usuário Criado com Sucesso"}

@router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_user(id: int, body: UserUpdateRequestDto, session: Session = Depends(get_db)):
    updated_user(id, body, session)
    return {"message": "Usuário Atualizado com Sucesso"}
