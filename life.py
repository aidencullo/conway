import pprint
import numpy as np
np.__version__
pp = pprint.PrettyPrinter(indent=4)

def row(size):
    return [0 for x in range(size)]

def random_grid(size):
    return [row(size) for x in range(size)]


class Board:

    def __init__(self, size):
        self.grid = random_grid(size)

    def print(self):
        pp.pprint(self.grid)
        print()

    def get(self, x, y):
        if x in range(0, len(self.grid)) and y in range(0,
        len(self.grid[0])):
            return self.grid[x][y]
        else:
            return 0

    def evolve(self):
        for (x, y), lement in np.ndenumerate(np.array(self.grid)):
            self.evolve_cell(x, y)

    def count_neighbors(self, x,y):
        count = 0
        count += self.get(x-1,y-1)
        count += self.get(x,y-1)
        count += self.get(x+1,y-1)
        count += self.get(x+1,y)
        count += self.get(x+1,y+1)
        count += self.get(x,y+1)
        count += self.get(x-1,y+1)
        count += self.get(x-1,y)
        return count

    def evolve_cell(self, x, y):
        count = self.count_neighbors(x, y)
        if self.get(x, y):
            print('active cell')
        else:
            print('dead cell')
        print(count)
        
board = Board(5)
board.evolve()
# board.evolve().print()
