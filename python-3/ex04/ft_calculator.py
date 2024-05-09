
class calculator:

    @staticmethod
    def size_check(fun) -> bool:
        def wrapper(*args):
            fun(args[1], args[2])
        return wrapper

    @classmethod
    @size_check
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        sum = 0
        for x, y in zip(V1, V2):
            sum += x * y
        print(f"Dot product is: {sum}")


    @classmethod
    @size_check
    def add_vec(V1: list[float], V2: list[float]) -> None:
        ret = []
        for x, y in zip(V1, V2):
            ret.append(x + y)
        print(f"Add Vector is : {ret}")
        
    @classmethod
    @size_check
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        ret = []
        for x, y in zip(V1, V2):
            ret.append(float(x - y))
        print(f"Sous Vector is: {ret}")
        

def main():
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a,b)
    calculator.add_vec(a,b)
    calculator.sous_vec(a,b)

if __name__ == "__main__":
    main()