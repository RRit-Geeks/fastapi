from typing import Optional
from src.models.product import Product
from fastapi import APIRouter, Query

router = APIRouter()
products_list: dict[int, Product] = {}


@router.post("/create")
def create_product(product: Product):
    if products_list.get(product.id, None):
        return product
    products_list[product.id] = product
    return product


@router.get("/all")
def get_all():
    return list(products_list.values())


@router.get("/{id}")  # Path Parameter/ Path Variable
def find_by_id(id: int, query_param: str):
    # print(id_)
    id_ = id
    return products_list.get(id_, None)


@router.put("/update/{id}")
def update_product(id: int, product: Product):
    if products_list.get(product.id, None):
        products_list[id] = product
        return product
    raise Exception(f"No Product found for id {id}")


@router.delete("/delete/{id}")
def delete_product(id: int):
    products_list.pop(id)
    return f"Deleted Successfully {id}"


@router.get("/{id}/{age}/{pincode}")  # Path Parameter/ Path Variable
def find_by_(age: int, id: int, pincode: str,  query_2: str, query_3: Optional[int] =12, query_param:str = None): # Query Parameter
    print(id, "     ", age, "     ", pincode, "     ", query_param)
    return products_list.get(id, None)
