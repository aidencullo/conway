import tools.constant as const
from tools.game import Game, generate_game

def main() -> None:
    game = generate_game(0)
    for _ in range(const.EVOLUTION_STEPS):
        game = game.evolve()
        game.print()

if __name__ == "__main__":
    main()
