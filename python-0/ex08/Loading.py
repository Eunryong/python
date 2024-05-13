
def ft_tqdm(lst: range) -> None:
    for i in lst:
        percetage = round(((i + 1) / lst.stop) * 100)
        prefix = (3 - len(str(percetage))) * " "
        bar = percetage * "█" + (100 - percetage) * " "
        yield i
        print(f"{prefix}{percetage}%|{bar}|{i + 1}/{lst.stop}", end="\r")


def main():
    print("hi")


if __name__ == "__main__":
    main()
