### Libraries

# standard
import time
import itertools

# third party
import numpy as np

# local modules
from grids import seed_grid
from prints import *

# globals
EVOLUTION_STEPS = 3
GRID_LENGTH = 10

def get(grid, x, y):
    try:
        return grid[x][y]
    except IndexError:
        return 0

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

if __name__ == "__main__":
    grid = seed_grid(GRID_LENGTH)
    for x in range(EVOLUTION_STEPS):
                 print_grid(grid)
                 grid = evolve(grid)
                 time.sleep(1)	
