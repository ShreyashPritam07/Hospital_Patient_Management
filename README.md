# Hospital Patient Management System

**VITyarthi Build Your Own Project**  
**Name:** Shreyash Pritam  
**Registration Number:** 26BAI11108  
**University:** VIT Bhopal University

## Overview
A menu-driven Python application that demonstrates basic patient-record management using functions, dictionaries/data models, lists, validation, modular programming, and CRUD-style operations.

## Features
1. Add Patient
2. Show Patients
3. Search Patient
4. Delete Patient
5. Exit

## Technologies
- Python 3
- Standard library only
- pytest for automated testing

## Project Structure
```text
Hospital_Patient_Management_VITyarthi/
├── src/
│   ├── main.py
│   ├── models.py
│   ├── operations.py
│   ├── repository.py
│   ├── service.py
│   ├── ui.py
│   └── validators.py
├── tests/
│   └── test_patient_management.py
├── docs/
│   ├── architecture.md
│   ├── diagrams/
│   └── screenshots/
├── README.md
├── statement.md
├── requirements.txt
└── .gitignore
```

## How to Run
From the project root:
```bash
python -m src.main
```

## Testing
Install pytest if needed:
```bash
pip install pytest
```
Run:
```bash
python -m pytest -q
```

## Notes
Patient records are stored in memory and are cleared when the application exits. This is intentionally a simple academic prototype; it is not a production medical-record system.
