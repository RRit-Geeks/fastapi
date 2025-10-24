from src.models.product import Product
from fastapi import APIRouter
router = APIRouter()
products_list: dict[int, Product] = {}

@router.post("/create")
def create_product(product: Product):
    if products_list.get(product.id, None):
        return product
    products_list[product.id]= product
    return product

@router.get("/all")
def get_all():
    return list(products_list.values())

@router.get("/{id}")
def find_by_id(id: int):
    return products_list.get(id, None)

@router.put("/update/{id}")
def update_product(id:int, product: Product):
    if products_list.get(product.id, None):
        products_list[id] = product
        return product
    raise Exception(f"No Product found for id {id}")

@router.delete("/delete/{id}")
def update_product(id:int):
    products_list.pop(id)
    return f"Deleted Successfully {id}"