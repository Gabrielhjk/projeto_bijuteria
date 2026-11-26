from backend.routes import login_router, user_router, product_router
from backend.models import *
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_origins=["*"],
    allow_headers=["*"],
)

app.include_router(user_router.router, prefix="/users", tags=["users"])
app.include_router(login_router.router, prefix="/login", tags=["login"])
app.include_router(product_router.router, prefix="/products", tags=["products"])