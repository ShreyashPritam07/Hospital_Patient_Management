# Architecture

The application uses a small layered structure:

- **UI layer:** `ui.py` displays menus and patient details.
- **Operations layer:** `operations.py` handles interactive menu actions.
- **Service layer:** `service.py` applies business rules and validation.
- **Repository layer:** `repository.py` stores and retrieves patient objects.
- **Model layer:** `models.py` defines the Patient data model.
- **Validation layer:** `validators.py` checks required fields.

The system uses in-memory storage through a Python list inside the repository. No database is required for this prototype.
