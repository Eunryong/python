
from sys import argv


def checkInt(string: str):
    if string[0].isdigit is False and string[0] != '-':
        return False
    if string[0] == '-' and len(string) == 1:
        return False
    for c in string[1:]:
        if c.isdigit() is False:
            return False
    return True


try:
    assert len(argv) <= 2, "more than one argument is provided"
    if len(argv) == 1:
        exit(0)
    assert checkInt(argv[1]) is True, "argument is not an integer"
    print("I'm Odd" if abs(int(argv[1]) % 2) == 1 else "I'm Even")
except AssertionError as e:
    print("AssertionError:", e)
    exit(1)
