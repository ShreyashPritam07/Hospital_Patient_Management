class PatientRepository:
    def __init__(self):
        self._patients = []

    def add(self, patient):
        self._patients.append(patient)

    def all(self):
        return list(self._patients)

    def find_by_name(self, name):
        target = name.strip().lower()
        for patient in self._patients:
            if patient.name.strip().lower() == target:
                return patient
        return None

    def delete_by_name(self, name):
        target = name.strip().lower()
        for patient in self._patients:
            if patient.name.strip().lower() == target:
                self._patients.remove(patient)
                return True
        return False

    def count(self):
        return len(self._patients)
