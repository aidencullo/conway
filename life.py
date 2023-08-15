import pprint
pp = pprint.PrettyPrinter(indent=4)

size = 5

def log(x):
    pp.pprint(x)

def row():
    return [0 for x in range(size)]

def printBoard():
    for x in board:
        print(*x)

def evolve(state):
    pass

class Board:

    def __init__(self):
        self.width = 0
        self.height = 0
        self.grid = [row() for x in range(size)]
        self.grid[2][2] = 1

    def __str__(self):
        return "under construction"

board = Board()
print(str(board))
