from backend.dto.product.product_request_dto import ProductRequestDto
from backend.dto.product.product_update_dto import ProductUpdateDto
from backend.models.products import Products
from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy import select


def get_all_products(session: Session):
    # faz a query 
    products_query = select(Products)

    # executa a query
    products = session.scalars(products_query).all()

    return products

def get_product_id(id: int, session: Session):
    # busca o produto na tabela de produtos que corresponde ao id 
    product = session.get(Products, id)

    if product is None:
        raise HTTPException(status_code=404, detail="Produto não Encontrado")

    return product

def created_product(body: ProductRequestDto, session: Session):
    # pega os dados do DTo e atribui ao model
    product = Products(
        product_name=body.product_name,
        unit_measurement=body.unit_measurement,
        base_price=body.base_price,
        weight=body.weight,
        description=body.description,
        obs=body.obs
    )

    # coloca o objeto do produto na sessao
    session.add(product)

    # envia para o banco de dados
    session.commit()

    # pega os dados atuais que estao no banco
    session.refresh(product)

    return product

def updated_product(id: int, body: ProductUpdateDto, session: Session):
    # busca o produto na tabela de produtos que corresponde ao id 
    product = session.get(Products, id)

    if product is None:
        raise HTTPException(status_code=404, detail="Produto não Encontrado")

    # atualiza os dados do produto com os dados do DTO
    product.product_name = body.product_name
    product.unit_measurement = body.unit_measurement
    product.base_price = body.base_price
    product.weight = body.weight
    product.description = body.description
    product.obs = body.obs
    product.active = body.active

    # envia para o banco de dados
    session.commit()

    # pega os dados atuais que estao no banco
    session.refresh(product)

    return product