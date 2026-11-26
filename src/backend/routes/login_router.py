from backend.services.login_service import login_service
from backend.db.db import get_db
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/", status_code=status.HTTP_200_OK)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_db)):
    return login_service(form_data, session)