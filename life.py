### Libraries

# standard
import random
import time

# local modules
from grids import grid

# global constants
enabled = False

def get(x, y):
    if x in range(0, len(grid)) and y in range(0, len(grid[0])):
        return grid[x][y]
    else:
        return 0

def evolve():
    new_grid = grid.copy()
    for (y, x) in np.ndenumerate(np.array(grid)):
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
    if get(x, y) and count not in range(2, 4):
        return 0
    if not get(x, y) and count == 3:
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

if __name__=="__main__":
    if enabled:
        i = 0
        while(i < steps):
            i += 1
            print_grid()
            grid = evolve()
            time.sleep(1)	
