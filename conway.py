# local modules
from tools.sample import seed_grid
import tools.constant as const
from tools.grid import Grid

def main() -> None:
    grid = seed_grid(const.SIDE_LENGTH)
    for _ in range(const.EVOLUTION_STEPS):
        grid = grid.evolve()
        grid.print()

if __name__ == "__main__":
    main()
