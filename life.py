#### Libraries

# standard
import random
import time

# third party
import numpy as np

size = 4

def row(size):
    return [random.randint(0, 1) for x in range(size)]

def repeating_row(size):
    return [1 if y == size // 2 else 0 for y in range(size)]

def random_grid(size):
    return [row(size) for x in range(size)]

def repeating_grid(size):
    return [repeating_row(size) for x in range(size)]

grid = repeating_grid(size)
# grid = random_grid(size)

def get(x, y):
    if x in range(0, len(grid)) and y in range(0, len(grid[0])):
        # print('in range')
        # print('x:{0}, y:{1}'.format(x,y))
        return grid[x][y]
    else:
        return 0

def evolve():
    new_grid = [*grid]
    for (y, x), element in np.ndenumerate(np.array(grid)):
        new_grid[x][y] = evolve_cell(x, y)
        print(x,y, element)
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
    # print('count: {0} get(x,y): {1}, x:{2}, y:{3}'.format(count, get(x,y),x,y))
    if get(x, y):
        if count not in range(2, 4):
            return 0
    else:
        if count == 3:
            return 1
    # print(grid[x][y])
    return grid[x][y]

def print_grid():
    print(*grid, sep='\n')
    print()

i = 0
while(i < 1):
    i += 1
    print_grid()
    grid = evolve()
    time.sleep(1)
