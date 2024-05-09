

def median(sorted_args) -> float:
    if len(sorted_args) % 2:
        return sorted_args[len(sorted_args) // 2]
    else :
        tmp = sorted_args[len(sorted_args) // 2] + sorted_args[len(sorted_args) // 2 - 1]
        return tmp / 2


def quartile(sorted_args) -> list:
    ret = []
    
    first = (len(sorted_args) - 1) * 1 // 4
    first_mod = (len(sorted_args) - 1) * 1 / 4 - first
    third = (len(sorted_args) - 1) * 3 // 4
    third_mod = (len(sorted_args) - 1) * 3 / 4 - third
    ret.append(sorted_args[first] + ((sorted_args[first + 1] - sorted_args[first]) * first_mod if len(sorted_args) > 1 else 0.0))
    ret.append(sorted_args[third] + ((sorted_args[third + 1] - sorted_args[third]) * third_mod if len(sorted_args) > 1 else 0.0))
    return ret


def ft_statistics(*args: any, **kwargs: any) -> None:
    for i in kwargs.values():
        if len(args) == 0 :
            print("ERROR")
            continue
        mean = sum(args) / len(args)
        sorted_args = sorted(args)
        if i == "mean":
            print(f"{i} : {mean}")
        elif i == "median":
            print(f"{i} : {median(sorted_args)}")
        elif i == "quartile":
            print(f"{i} : {quartile(sorted_args)}")
        elif i == "std":
            print(f"{i} : {pow(sum([pow(val - mean, 2) for val in args]) / len(args), 1 / 2)}")
        elif i == "var":
            print(f"{i} : {sum([pow(val - mean, 2) for val in args]) / len(args)}")


def main():
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")

if __name__ == "__main__":
    main()