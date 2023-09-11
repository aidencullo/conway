# standard
import itertools
import time

# third party
import numpy as np

# local
import tools.constant as const

class Grid:
    """
    A simple, square grid
    TODO: implement operator dec
    """

    def __init__(self, grid = None):
        if grid is None:
            grid = np.zeros((const.SIDE_LENGTH, const.SIDE_LENGTH))
        else:
            grid = np.ones((const.SIDE_LENGTH, const.SIDE_LENGTH))
        self._grid = grid

    def __setitem__(self, item, value):
        self._grid[item] = value

    def __getitem__(self, indices):
        try:
            return self._grid[indices]
        except IndexError:
            return 0

    def __eq__(self, other):
        return np.array_equal(self._grid, other._grid)

    def evolve(self):
        new_grid = Grid()
        for (y, x), value in np.ndenumerate(self._grid):
            new_grid[x, y] = self.evolve_cell(x, y)
        return new_grid

    def count_neighbors(self, x, y):
        count = sum(self[x + i, y + k] for i, k in itertools.product(range(-1, 2), range(-1, 2)))
        return count - self[x, y]

    def evolve_cell(self, x, y):
        count = self.count_neighbors(x, y)
        if self[x, y] and count not in range(2, 4):
            return 0
        if not self[x, y] and count == 3:
            return 1
        return self[x, y]

    def transpose(self):
        return Grid(self._grid.transpose())
    
    def print(self):
        for y in self._grid:
            for x in y:
                print('x ' if x else '_ ', end='')
            print()
