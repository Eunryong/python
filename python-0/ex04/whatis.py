
from sys import argv

try:
    assert len(argv) <= 2, "more than one argument is provided"
    if len(argv) == 1:
        exit(0)
    assert argv[1].isdigit , "argument is not an integer"
    print("I'm Odd" if int(argv[1]) % 2 == 1 else "I'm Even")
except AssertionError as e:
    print("AssertionError:", e)
    exit(1)
