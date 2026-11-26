from backend.dto.product.product_request_dto import ProductRequestDto
from backend.dto.product.product_response_dto import ProductResponseDto
from backend.dto.product.product_update_dto import ProductUpdateRequestDto
from backend.security.authorization import require_admin
from backend.services.product_service import created_product, get_all_products, get_product_id, updated_product
from backend.db.db import get_db
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", response_model=list[ProductResponseDto], status_code=status.HTTP_200_OK)
async def get_products(session: Session = Depends(get_db)):
    products = get_all_products(session)
    return products

@router.get("/{id}", response_model=ProductResponseDto, status_code=status.HTTP_200_OK)
async def get_product(id: int, session: Session = Depends(get_db)):
    product = get_product_id(id, session)
    return ProductResponseDto.model_validate(product)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_product(body: ProductRequestDto, session: Session = Depends(get_db)):
    created_product(body, session)
    return {"message": "Produto Criado com Sucesso"}

@router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_product(id: int, body: ProductUpdateRequestDto, session: Session = Depends(get_db)):
    updated_product(id, body, session)
    return {"message": "Produto Atualizado com Sucesso"}

