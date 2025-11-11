from fastapi import APIRouter
from src.models.doctor import Doctor
from src.utils.service_objects_injection_utils import createDoctorsServiceObj

doctors_endpoint_router= APIRouter()

service = createDoctorsServiceObj()

# Dependency Injection

@doctors_endpoint_router.post("/add")
def add_doctor(doctor: Doctor):
    return service.add_doctor(doctor)

@doctors_endpoint_router.get("/all")
def get_all_doctors():
    return service.get_all_doctors()

@doctors_endpoint_router.get("/{id}")  
def get_doctor(id: int):
    return service.get_doctor(id)

@doctors_endpoint_router.delete("/{id}")  
def delete_doctor(id: int):
    return service.delete_doctor(id)