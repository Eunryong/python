from ft_filter import ft_filter
from sys import argv

# def lenCheck(string):
#     return len(string) > int(argv[2])

if __name__ == '__main__':
    try:
        punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        assert len(argv) == 3 and (1 for c in argv[1] if c not in punctuation) and argv[2].isdigit(), "the argument are bad"
        string = argv[1].split(" ")
        print(ft_filter(lambda x: len(x) > int(argv[2]), string))
        print(ft_filter.__doc__)
    except AssertionError as e:
        print("AssertionError:", e)
        exit(1)
