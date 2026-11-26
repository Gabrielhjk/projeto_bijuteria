from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import jwt
import os

load_dotenv(".env")

secret_key = os.getenv("SECRET_KEY")
algorithm = os.getenv("ALGORITHM")

def create_access_token(payload: dict):
    to_encode = payload.copy()
    token_expire = datetime.now(timezone.utc) + timedelta(hours=2)
    to_encode.update({"exp": token_expire})

    encoded_jwt = jwt.encode(
        to_encode,
        secret_key,
        algorithm=algorithm
    )

    return encoded_jwt

def decode_access_token(token):
    decode_jwt = jwt.decode(
        token,
        secret_key,
        algorithms=[algorithm]
    ) 

    return decode_jwt