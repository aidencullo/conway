import tools.constant as const
from tools.game import Game, beacon, glider, beehive, glider_end
from tools.help import game_help, command_error
from tools.evolution import run

def main() -> None:
    print('starting config')
    game = glider()
    game.print()
    while 1:
        choice = input()
        if choice == 'step':
            game = game.evolve()
            game.print()
        elif choice == 'reset':
            game = glider()
            game.print()
        elif choice == 'start':
            run(game)
        elif choice == 'glider':
            game = glider()
            game.print()            
        elif choice == 'beacon':
            game = beacon()
            game.print()
        elif choice == 'beehive':
            game = beehive()
            game.print()
        else:
            command_error()
            game_help()

if __name__ == "__main__":
    main()
