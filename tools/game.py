import itertools
import time

import numpy as np

import tools.constant as const

def glider():
    game = Game()
    game[0, 1] = 1
    game[1, 2] = 1
    game[2, 0] = 1
    game[2, 1] = 1
    game[2, 2] = 1
    return game

def glider_end():
    game = Game()
    game[1, 2] = 1
    game[2, 3] = 1
    game[3, 1] = 1
    game[3, 2] = 1
    game[3, 3] = 1
    return game

def beehive():
    game = Game()
    game[5, 5] = 1
    game[5, 6] = 1
    game[6, 7] = 1
    game[7, 5] = 1
    game[7, 6] = 1
    game[6, 4] = 1
    return game

def beacon():
    game = Game()
    game[5, 5] = 1
    game[5, 6] = 1
    game[6, 5] = 1
    game[7, 8] = 1
    game[8, 7] = 1
    game[8, 8] = 1
    return game

class Game:
    """
    A simple, square grid

    >>> Game() == Game()
    True
    >>> Game() == beehive()
    False
    >>> g = beehive()
    >>> g.evolve() ==  g
    True
    >>> beehive().evolve() == beehive()
    True
    >>> beehive().evolve(2) == beehive()
    True
    >>> glider() != glider().evolve()
    True
    >>> beacon() != beacon().evolve()
    True
    >>> beacon() == beacon().evolve(2)
    True
    >>> glider().evolve(4) == glider_end()
    True
    >>> glider().evolve(5) == glider_end()
    False

    todo
    
    interactive
    action to run tests
    
    """

    def __init__(self, grid = None):
        grid_copy = grid
        if grid is None:
            grid_copy = np.zeros((const.SIDE_LENGTH, const.SIDE_LENGTH))
        self._grid = grid_copy

    def __setitem__(self, item, value):
        self._grid[item] = value

    def __getitem__(self, indices):
        try:
            return self._grid[indices]
        except IndexError:
            return 0
        
    def __eq__(self, other):
        return np.array_equal(self._grid, other._grid)

    @property
    def grid(self):   
        print("getter method")   
        return self._grid

    @grid.setter 
    def grid(self, other):
        print("setter method")   
        self._grid = other

    def evolve(self, count = 1):
        for x in range(count):
            new_grid = Game()
            for (y, x), value in np.ndenumerate(self._grid):
                new_grid[x, y] = self.evolve_cell(x, y)
        if count != 1:
            return new_grid.evolve(count - 1)
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
        return Game(self._grid.transpose())
    
    def print(self):
        for y in self._grid:
            for x in y:
                print('x ' if x else '_ ', end='')
            print()
        print()
