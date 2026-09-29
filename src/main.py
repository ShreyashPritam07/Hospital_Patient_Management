from .operations import add_patient, show_patients, search_patient, delete_patient
from .repository import PatientRepository
from .service import PatientService
from .ui import show_menu

def main():
    service = PatientService(PatientRepository())
    while True:
        show_menu()
        choice = input('Enter your choice: ')
        if choice == '1':
            add_patient(service)
        elif choice == '2':
            show_patients(service)
        elif choice == '3':
            search_patient(service)
        elif choice == '4':
            delete_patient(service)
        elif choice == '5':
            print('\nThank you for using the system.')
            break
        else:
            print('\nInvalid choice. Please try again.')

if __name__ == '__main__':
    main()
