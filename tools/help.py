def game_help():
    print('---------------')
    print('Welcome to the interactive conways game of life')
    print()
    print("Commands:")
    print('    step    -- evolve game once')
    print('    reset   -- reset to glider')
    print('    start   -- begin evolution')
    print('    beehive   -- load beehive')
    print('    beacon   -- load beacon')
    print('    glider   -- load glider')
    print('---------------')

def command_error():
    print('---------------')
    print("unrecognized input")
    print('---------------')
