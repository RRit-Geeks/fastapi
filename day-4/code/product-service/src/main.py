from fastapi import FastAPI
from src.endpoints.product_endpoints import router
app = FastAPI()

app.include_router(router)
