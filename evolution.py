### Libraries

# standard
import itertools
import time

# third party
import numpy as np

# local
from prints import print_grid

def get(grid, x, y):
    try:
        return grid[x][y]
    except IndexError:
        return 0


def ui_wrap(func):
    def wrapped(grid):
        print_grid(grid)
        grid = func(grid)
        time.sleep(1)
        return grid
    return wrapped    
    
@ui_wrap
def evolve(grid):
    new_grid = grid.copy()
    for (y, x), value in np.ndenumerate(grid):
        new_grid[x][y] = evolve_cell(grid, x, y)
    return new_grid

def count_neighbors(grid, x,y):
    count = sum(get(grid, x + i, y + k) for i, k in itertools.product(range(-1, 2), range(-1, 2)))
    return count - get(grid, x, y)

def evolve_cell(grid, x, y):
    count = count_neighbors(grid, x, y)
    if get(grid, x, y) and count not in range(2, 4):
        return 0
    if not get(grid, x, y) and count == 3:
        return 1
    return grid[x][y]
