### Libraries

# standard
import random
import time

# third party
import numpy as np

size = 10
steps = 10
enabled = True

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

def get(x, y):
    if x in range(0, len(grid)) and y in range(0, len(grid[0])):
        return grid[x][y]
    else:
        return 0

def copy_grid(grid):
     return grid.copy()

def evolve():
    new_grid = copy_grid(grid)
    for (y, x), element in np.ndenumerate(np.array(grid)):
        new_grid[x][y] = evolve_cell(x, y)
    return new_grid

def count_neighbors( x,y):
    count = 0
    count += get(x-1,y-1)
    count += get(x,y-1)
    count += get(x+1,y-1)
    count += get(x+1,y)
    count += get(x+1,y+1)
    count += get(x,y+1)
    count += get(x-1,y+1)
    count += get(x-1,y)
    return count

def evolve_cell( x, y):
    count = count_neighbors(x, y)
    if get(x, y):
        if count not in range(2, 4):
            return 0
    else:
        if count == 3:
            return 1
    return grid[x][y]

def print_grid():
    for row in grid:
        line = ''
        for item in row:
            if item == 0:
                line += '-' 
            else:
                line += 'x' 
        print(line)

grid = beacon(size)

if __name__=="__main__":
    print('hello world')
    if enabled:
        i = 0
        while(i < steps):
            i += 1
            print_grid()
            grid = evolve()
            time.sleep(1)	
