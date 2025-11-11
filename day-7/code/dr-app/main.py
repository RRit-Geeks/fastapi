from fastapi import FastAPI
from src.endpoints.health_check import health_router
from src.endpoints.doctors_endpoint import doctors_endpoint_router

app = FastAPI(
    title="Doctors Appointment Booking Application",
    version="1.0.0",
    root_path="/doctors-app",
    docs_url="/docs",  # Swagger UI URL
    redoc_url="/redoc",  # ReDoc URL
    openapi_url="/openapi.json",
)

app.include_router(health_router, prefix="/status", tags=["Health"])
app.include_router(
    doctors_endpoint_router, prefix="/doctors", tags=["Doctors Endpoints"]
)
