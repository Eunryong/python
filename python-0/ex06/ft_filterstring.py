from ft_filter import ft_filter
from sys import argv

# def lenCheck(string):
#     return len(string) > int(argv[2])

if __name__ == '__main__':
    try:
        punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        error_message = "the argument are bad"
        assert len(argv) == 3, error_message
        assert (1 for c in argv[1] if c not in punctuation), error_message
        assert argv[2].isdigit(), error_message
        string = argv[1].split(" ")
        print(ft_filter(lambda x: len(x) > int(argv[2]), string))
        print(ft_filter.__doc__)
    except AssertionError as e:
        print("AssertionError:", e)
        exit(1)
