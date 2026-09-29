def validate_patient_fields(name, age, gender, disease, phone):
    if not name.strip():
        raise ValueError('Patient name cannot be empty.')
    if not age.strip():
        raise ValueError('Patient age cannot be empty.')
    if not gender.strip():
        raise ValueError('Gender cannot be empty.')
    if not disease.strip():
        raise ValueError('Disease/problem cannot be empty.')
    if not phone.strip():
        raise ValueError('Phone number cannot be empty.')
    return True
