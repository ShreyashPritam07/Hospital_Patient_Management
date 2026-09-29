def add_patient(service):
    print('\nAdd Patient')
    name = input('Enter patient name: ')
    age = input('Enter patient age: ')
    gender = input('Enter gender: ')
    disease = input('Enter disease/problem: ')
    phone = input('Enter phone number: ')
    try:
        service.add_patient(name, age, gender, disease, phone)
        print('\nPatient added successfully.')
    except ValueError as exc:
        print('\nError:', exc)

def show_patients(service):
    print('\nPatient Details')
    patients = service.get_patients()
    if not patients:
        print('No patient records found.')
        return
    for i, patient in enumerate(patients, start=1):
        print('\nPatient', i)
        from .ui import display_patient
        display_patient(patient)

def search_patient(service):
    print('\nSearch Patient')
    name = input('Enter patient name: ')
    patient = service.search_patient(name)
    if patient:
        print('\nPatient found!')
        from .ui import display_patient
        display_patient(patient)
    else:
        print('Patient not found.')

def delete_patient(service):
    print('\nDelete Patient')
    name = input('Enter patient name: ')
    if service.delete_patient(name):
        print('Patient record deleted.')
    else:
        print('Patient not found.')
