import time

# local modules
from prints import print_grid
from grids import seed_grid
from evolution import evolve 

# globals
EVOLUTION_STEPS = 3
GRID_LENGTH = 10

if __name__ == "__main__":
    grid = seed_grid(GRID_LENGTH)
    for x in range(EVOLUTION_STEPS):
        print_grid(grid)
        grid = evolve(grid)
        time.sleep(1)	
