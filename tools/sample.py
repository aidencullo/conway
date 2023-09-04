# third party
import numpy as np

from .grid import Grid

# default from https://playgameoflife.com/
def test_grid_1(size):
    grid = Grid()
    grid[5, 5] = 1
    grid[6, 6] = 1
    grid[6, 7] = 1
    grid[5, 7] = 1
    grid[4, 7] = 1
    return grid.transpose()

def beehive(size):
    grid = Grid()
    grid[5, 5] = 1
    grid[5, 6] = 1
    grid[6, 7] = 1
    grid[7, 5] = 1
    grid[7, 6] = 1
    grid[6, 4] = 1
    return grid

def beacon(size):
    grid = Grid()
    grid[5, 5] = 1
    grid[5, 6] = 1
    grid[6, 5] = 1
    grid[7, 8] = 1
    grid[8, 7] = 1
    grid[8, 8] = 1
    return grid

def seed_grid(size):
    return test_grid_1(size)
