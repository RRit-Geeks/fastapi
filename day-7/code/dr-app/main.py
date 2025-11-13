from fastapi import FastAPI
from src.endpoints.health_check import health_router
from src.endpoints.doctors_endpoint import doctors_endpoint_router
import logging

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
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(filename)s - Line %(lineno)d - %(message)s",
        },
        "verbose": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(filename)s - Line %(lineno)d - %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "app.log",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}

# Apply logging configuration
logging.config.dictConfig(LOGGING_CONFIG)