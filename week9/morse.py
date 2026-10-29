
class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


# Each entry contains a letter and its Morse code.
table = [
    ('A', '.-'), ('B', '-...'), ('C', '-.-.'),
    ('D', '-..'), ('E', '.'), ('F', '..-.'),
    ('G', '--.'), ('H', '....'), ('I', '..'),
    ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
    ('M', '--'), ('N', '-.'), ('O', '---'),
    ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),
    ('S', '...'), ('T', '-'), ('U', '..-'),
    ('V', '...-'), ('W', '.--'), ('X', '-..-'),
    ('Y', '-.--'), ('Z', '--..')
]


def make_morse_tree():
    root = TNode(None, None, None)

    for tp in table:
        code = tp[1]
        node = root

        for c in code:
            if c == '.':
                if node.left is None:
                    node.left = TNode(None, None, None)
                node = node.left
            elif c == '-':
                if node.right is None:
                    node.right = TNode(None, None, None)
                node = node.right

        node.data = tp[0]

    return root


def decode(root, code):
    node = root

    for c in code:
        if c == '.':
            node = node.left
        elif c == '-':
            node = node.right

        if node is None:
            return "Invalid Morse code"

    return node.data if node.data is not None else "No letter found"


# Run the program
root = make_morse_tree()

morse_code = input("Enter Morse code (e.g. ...): ")
result = decode(root, morse_code)
print("Decoded letter:", result)
