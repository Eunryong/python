from sys import argv


def printMorse(s):
    temp = []
    morseCode = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.', ' ': '/'
    }
    for c in s:
        temp.append(morseCode[c.upper()])
    print(" ".join(temp))


def stringCheck(s: str):
    for c in s:
        if not c.isalnum() and c != ' ':
            return False
    return True


if __name__ == '__main__':
    try:
        assert len(argv) == 2 and stringCheck(argv[1]), "the argument are bad"
        printMorse(argv[1])
    except AssertionError as e:
        print("AssertionError:", e)
        exit(1)
