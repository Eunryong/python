import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    # login: str
    id: str = field(default_factory=generate_id)

    

def main():
    student = Student(name = "Edward", surname = "agle", id="123")
    print(student)

if __name__ == "__main__":
        main()