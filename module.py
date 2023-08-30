# local modules
from grids import seed_grid
from evolution import evolve 

# globals
EVOLUTION_STEPS = 3
GRID_LENGTH = 10

def main() -> None:
    grid = seed_grid(GRID_LENGTH)
    for _ in range(EVOLUTION_STEPS):
        grid = evolve(grid)

if __name__ == "__main__":
    main()
