from abc import ABC, abstractmethod


class Character(ABC):
    '''hi'''
    
    @abstractmethod
    def __init__(self, first_name, is_alive):
        '''Character constructor'''
        pass

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    '''hi'''

    def __init__(self, first_name, is_alive=True):
        '''Stark constructor'''
        self.first_name = first_name
        self.is_alive = is_alive
    
    def die(self):
        '''kill Stark'''
        self.is_alive = False


def main():
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)
    # hodor = Character("hodor")


if __name__ == "__main__":
    main()
