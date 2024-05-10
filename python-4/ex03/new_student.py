import random
import string
from dataclasses import dataclass, field



def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
    name: string
    surname: string
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        self.login = self.name[0] + self.surname if len(self.name) > 0 else self.surname


def main():
    student = Student(name = "qwe", surname = "")
    print(student)

if __name__ == "__main__":
        main()