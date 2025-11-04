from typing import Optional
from src.models.product import Product

class ProductService:
    """
    Service Methods for dealing with CRUD operations.
    
    """
    def __init__(self):
        self.products_list: dict[int, Product] = {}

    def create_product(self, product: Product): # Object Level Method.
        if self.products_list.get(product.id, None):
            return product
        self.products_list[product.id] = product
        return product
    
    def get_all(self):
        return list(self.products_list.values())
    
    def find_by_id(self, id: int):
        return self.products_list.get(id, None)
    
    def update_product(self, id: int, product: Product):
        if self.products_list.get(product.id, None):
            self.products_list[id] = product
            return product
        raise Exception(f"No Product found for id {id}")
    
    def delete_product(self, id: int):
        self.products_list.pop(id)
        return f"Deleted Successfully {id}"
    
    def find_by_(self, age: int, id: int, pincode: str,  query_2: str, query_3: Optional[int] =12, query_param:str = None): # Query Parameter
        print(id, "     ", age, "     ", pincode, "     ", query_param)
        return self.products_list.get(id, None)