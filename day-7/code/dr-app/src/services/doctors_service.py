from src.models.doctor import Doctor


class DoctorService:
    def __init__(self):
        self.doctors: dict[int, Doctor] = {}

    def add_doctor(self, doctor: Doctor):
        self.doctors[doctor.id] = doctor
        return {"message": "Doctor added successfully", "data": doctor}

    def get_all_doctors(self):
        return list(self.doctors.values())

    def get_doctor(self, id: int):
        return self.doctors.get(id, {"error": "Doctor not found"})

    def delete_doctor(self, id: int):
        if id in self.doctors:
            del self.doctors[id]
            return {"message": f"Doctor {id} deleted successfully"}
        return {"error": "Doctor not found"}
