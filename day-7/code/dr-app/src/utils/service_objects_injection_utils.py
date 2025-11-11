""" Handles creation of all the Service Objects. """
from src.services.doctors_service import DoctorService


def createDoctorsServiceObj():
    """Creating an Object of DoctorService"""
    print("I am getting created.")
    return DoctorService()
