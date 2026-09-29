from src.models import Patient
from src.repository import PatientRepository
from src.service import PatientService


def make_service():
    return PatientService(PatientRepository())


def test_add_and_list_patient():
    service = make_service()
    p = service.add_patient('Aarav', '20', 'Male', 'Fever', '9876543210')
    assert p.name == 'Aarav'
    assert len(service.get_patients()) == 1


def test_search_is_case_insensitive():
    service = make_service()
    service.add_patient('Priya', '21', 'Female', 'Cold', '9999999999')
    assert service.search_patient('priya').disease == 'Cold'


def test_delete_patient():
    service = make_service()
    service.add_patient('Rahul', '25', 'Male', 'Cough', '8888888888')
    assert service.delete_patient('rahul') is True
    assert service.search_patient('Rahul') is None


def test_delete_missing_patient():
    service = make_service()
    assert service.delete_patient('Nobody') is False


def test_validation_rejects_empty_name():
    service = make_service()
    try:
        service.add_patient('', '20', 'Male', 'Fever', '1234567890')
    except ValueError as exc:
        assert 'name' in str(exc).lower()
    else:
        raise AssertionError('Expected ValueError')


def test_patient_to_dict():
    patient = Patient('A', '18', 'Female', 'Flu', '123')
    assert patient.to_dict()['disease'] == 'Flu'
