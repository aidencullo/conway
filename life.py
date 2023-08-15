import pprint
import numpy as np
np.__version__
pp = pprint.PrettyPrinter(indent=4)

def row():
    return [0 for x in range(size)]

def evolve(board):
    for (x, y), element in np.ndenumerate(np.array(board.grid)):
        print(x, y, element)
        evolve_cell(board.grid, x, y)

def evolve_cell(grid, x, y):
    pass
        
class Board:

    def __init__(self, size):
        self.grid = [row() for x in range(size)]
        self.grid[2][2] = 1

    def print(self):
        pp.pprint(self.grid)
        print()
        
board = Board(5)
board.print()
evolve(board)
board.print()
