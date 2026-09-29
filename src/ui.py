def display_patient(patient):
    print('Name :', patient.name)
    print('Age :', patient.age)
    print('Gender :', patient.gender)
    print('Disease :', patient.disease)
    print('Phone :', patient.phone)

def show_menu():
    print('\n==============================')
    print(' HOSPITAL PATIENT MANAGEMENT')
    print('==============================')
    print('1. Add Patient')
    print('2. Show Patients')
    print('3. Search Patient')
    print('4. Delete Patient')
    print('5. Exit')
    print('==============================')
