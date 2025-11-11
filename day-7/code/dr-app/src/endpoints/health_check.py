from fastapi import APIRouter


health_router= APIRouter()
@health_router.get("/health")
def health():
    return "I am up and running."