from S1E9 import Character

class Baratheon(Character):
    '''Baratheon'''
    
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hair = "dark"
        

    def __str__(self):
        pass
    
    def __repr__(self) -> str:
        return "Vector: ('{}', '{}', '{}')".format(self.family_name, self.eyes, self.hair)
    
    def die(self):
        self.is_alive = False


class Lannister(Character):
    '''Lannister'''

    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hair = "light"

    def __str__(self):
        pass
    
    def __repr__(self) -> str:
        return "Vector: ('{}', '{}', '{}')".format(self.family_name, self.eyes, self.hair)
    
    def die(self):
        self.is_alive = False
        
    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        cls = Lannister(first_name, is_alive)
        return cls
    


def main():
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")
    Jaine = Lannister.create_lannister("Jaine", True)
    print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")


if __name__ == "__main__":
    main()