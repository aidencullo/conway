import time

from tools.game import glider

def run(game):
    while 1:
        time.sleep(1)
        game = game.evolve()
        game.print()
        
