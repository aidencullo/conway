# third party
import numpy as np

def row(size, num):
    return [num for x in range(size)]

def random_row(size):
    return [random.randint(0, 1) for x in range(size)]

def random_grid(size):
    return [random_row(size) for x in range(size)]

def repeating_grid(size):
    def repeating_row(size):
        return [1 if y == size // 2 else 0 for y in range(size)]
    return [repeating_row(size) for x in range(size)]

def zero_grid(size):
    return np.zeros((size, size))

# default from https://playgameoflife.com/
def test_grid_1(size):
    grid = zero_grid(size)
    grid[5][5] = 1
    grid[6][6] = 1
    grid[6][7] = 1
    grid[5][7] = 1
    grid[4][7] = 1
    return grid.transpose()

def beehive(size):
    grid = zero_grid(size)
    grid[5][5] = 1
    grid[5][6] = 1
    grid[6][7] = 1
    grid[7][5] = 1
    grid[7][6] = 1
    grid[6][4] = 1
    return grid

def beacon(size):
    grid = zero_grid(size)
    grid[5][5] = 1
    grid[5][6] = 1
    grid[6][5] = 1

    grid[7][8] = 1
    grid[8][7] = 1
    grid[8][8] = 1

    return grid

def seed_grid(size):
    return beacon(size)
