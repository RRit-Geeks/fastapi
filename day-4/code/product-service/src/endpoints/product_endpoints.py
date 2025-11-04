from typing import Optional
from src.models.product import Product
from src.services.product_service import ProductService
from fastapi import APIRouter, Query

router = APIRouter()

#Creating an Object
product_service = ProductService()

@router.post("/create")
def create_product(product: Product):
    return product_service.create_product(product=product)


@router.get("/all")
def get_all():
    return product_service.get_all()


@router.get("/{id}")  # Path Parameter/ Path Variable
def find_by_id(id: int):
    return product_service.find_by_id(id=id)


@router.put("/update/{id}")
def update_product(id: int, product: Product):
    return product_service.update_product(id=id, product=product)


@router.delete("/delete/{id}")
def delete_product(id: int):
    return product_service.delete_product(id=id)


@router.get("/{id}/{age}/{pincode}")  # Path Parameter/ Path Variable
def find_by_(age: int, id: int, pincode: str,  query_2: str, query_3: Optional[int] =12, query_param:str = None): # Query Parameter
    return product_service.find_by_(age=age, id=id, pincode=pincode, query_2=query_2)
