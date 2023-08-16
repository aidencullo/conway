import pprint
import numpy as np
np.__version__
pp = pprint.PrettyPrinter(indent=4)

def row(size):
    return [0 for x in range(size)]

def evolve(board):
    for (x, y), element in np.ndenumerate(np.array(board.grid.value)):
        evolve_cell(board.grid, x, y)

def evolve_cell(grid, x, y):
    print(grid.get(x + 1, y))
    print(grid.get(x, y))
    print(grid.get(x - 1, y))
          
class Grid:    

    def __init__(self, size):
        self.value = [row(size) for x in range(size)]
        self.value[2][2] = 1

    def get(self, x, y):
        return x in range(0, len(self.value))
        
class Board:

    def __init__(self, size):
        self.grid = Grid(size)

    def print(self):
        pp.pprint(self.grid)
        print()
        
board = Board(5)
board.print()
evolve(board)
board.print()
