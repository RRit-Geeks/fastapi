""" Handles creation of all the Service Objects. """
from src.services.doctors_service import DoctorService
from functools import lru_cache

@lru_cache
def createDoctorsServiceObj():
    """Creating an Object of DoctorService"""
    print("I am getting created.")
    return DoctorService() #Statefull Object
