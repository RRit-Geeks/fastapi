from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    category: str
    price: float
    other_details: dict[str, str]
