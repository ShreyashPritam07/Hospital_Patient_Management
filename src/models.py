from dataclasses import dataclass, asdict

@dataclass
class Patient:
    name: str
    age: str
    gender: str
    disease: str
    phone: str

    def to_dict(self):
        return asdict(self)
