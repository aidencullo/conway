def print_grid(grid):
    for row in grid:
        line = ''
        for item in row:
            if item == 0:
                line += '-' 
            else:
                line += 'x' 
        print(line)
    print()
