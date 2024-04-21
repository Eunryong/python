from sys import argv, stdin;

def building(s: str):
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    print(f"The text contains {len(s)} characters:")
    print(f"{sum(1 for c in s if c.isupper())} upper letters")
    print(f"{sum(1 for c in s if c.islower())} lower letters")
    print(f"{sum(1 for c in s if c in punctuation)} punctuation marks")
    print(f"{sum(1 for c in s if c.isspace())} spaces")
    print(f"{sum(1 for c in s if c.isdigit())} digits")

if __name__ == '__main__':
    try:
        assert len(argv) <= 2, "more than one argument is provided"
        if (len(argv) == 1):
            # s = input("What is the text to count?\n")
            print("What is the text to count?")
            s = stdin.readline()
        else:
            s = argv[1]
        building(s)
    except AssertionError as e:
        print("AssertionError:", e)
        exit(1)
