from .models import Patient
from .validators import validate_patient_fields

class PatientService:
    def __init__(self, repository):
        self.repository = repository

    def add_patient(self, name, age, gender, disease, phone):
        validate_patient_fields(name, age, gender, disease, phone)
        patient = Patient(name.strip(), age.strip(), gender.strip(), disease.strip(), phone.strip())
        self.repository.add(patient)
        return patient

    def get_patients(self):
        return self.repository.all()

    def search_patient(self, name):
        return self.repository.find_by_name(name)

    def delete_patient(self, name):
        return self.repository.delete_by_name(name)
