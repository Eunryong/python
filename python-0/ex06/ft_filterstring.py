from ft_filter import ft_filter
import sys

# def lenCheck(string):
#     return len(string) > int(argv[2])

def main():
    try:
        punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        error_message = "the argument are bad"
        assert len(sys.argv) == 3, error_message
        assert (1 for c in sys.argv[1] if c not in punctuation), error_message
        assert sys.argv[2].isdigit(), error_message
        string = sys.argv[1].split(" ")
        print(ft_filter(lambda x: len(x) > int(sys.argv[2]), string))
        print(ft_filter.__doc__)
    except AssertionError as e:
        print("AssertionError:", e)
        exit(1)


if __name__ == '__main__':
    main()
