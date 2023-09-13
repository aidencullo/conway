import tools.constant as const
from tools.game import Game, beacon, glider, beehive, glider_end

def main() -> None:
    game = glider_end()
    print('starting config')
    game.print()
    for step in range(const.EVOLUTION_STEPS):
        print(f"Step {step}")
        game = game.evolve()
        game.print()

if __name__ == "__main__":
    main()
