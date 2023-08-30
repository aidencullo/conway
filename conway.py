# local modules
from tools.grids import seed_grid
from tools.evolution import evolve
import tools.constants as const

def main() -> None:
    grid = seed_grid(const.GRID_LENGTH)
    for _ in range(const.EVOLUTION_STEPS):
        grid = evolve(grid)

if __name__ == "__main__":
    main()
