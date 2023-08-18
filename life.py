import random
import time
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
        return grid[x][y]
    else:
        return 0

def evolve():
    new_grid = [*grid]
    for (x, y), element in np.ndenumerate(np.array(grid)):
        new_cell = evolve_cell(x, y)
        new_grid[x][y] = new_cell
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
    print(*grid, sep='\n')
    print()

i = 0
while(i < 4):
    i += 1
    print_grid()
    grid = evolve()
    time.sleep(1)
