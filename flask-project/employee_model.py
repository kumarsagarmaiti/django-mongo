from dataclasses import dataclass
from dataclass_wizard import JSONWizard


@dataclass
class Employee(JSONWizard):
    name: str
    age: int
    email: str
    department: str
