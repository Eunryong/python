import sys


def building(s: str):
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    print(f"The text contains {len(s)} characters:")
    print(f"{sum(1 for c in s if c.isupper())} upper letters")
    print(f"{sum(1 for c in s if c.islower())} lower letters")
    print(f"{sum(1 for c in s if c in punctuation)} punctuation marks")
    print(f"{sum(1 for c in s if c.isspace())} spaces")
    print(f"{sum(1 for c in s if c.isdigit())} digits")


def main():
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if (len(sys.argv) == 1):
            print("What is the text to count?")
            s = sys.stdin.readline()
        else:
            s = sys.argv[1]
        building(s)
    except AssertionError as e:
        print("AssertionError:", e)
        exit(1)


if __name__ == '__main__':
    main()
