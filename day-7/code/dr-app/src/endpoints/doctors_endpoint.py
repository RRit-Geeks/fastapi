from fastapi import APIRouter, Depends
from src.models.doctor import Doctor
from src.utils.service_objects_injection_utils import createDoctorsServiceObj
from src.services.doctors_service import DoctorService
import logging
doctors_endpoint_router = APIRouter()

# service = createDoctorsServiceObj() Hardcoded..

# Dependency Injection


@doctors_endpoint_router.post("/add")
def add_doctor(
    doctor: Doctor, service: DoctorService = (Depends(createDoctorsServiceObj))
):
    logging.info("Adding a doctor with id : %s", doctor.id)
    return service.add_doctor(doctor)


@doctors_endpoint_router.get("/all")
def get_all_doctors(service: DoctorService = (Depends(createDoctorsServiceObj))):
    return service.get_all_doctors()


@doctors_endpoint_router.get("/{id}")
def get_doctor(id: int, service: DoctorService = (Depends(createDoctorsServiceObj))):
    return service.get_doctor(id)


@doctors_endpoint_router.delete("/{id}")
def delete_doctor(id: int, service: DoctorService = (Depends(createDoctorsServiceObj))):
    return service.delete_doctor(id)
