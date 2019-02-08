def print_grid(board):
    """
    Taken from https://stackoverflow.com/questions/37952851/formating-sudoku-grids-python-3
    """
    print("+" + "---+"*9)
    for i, row in enumerate(board):
        print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
        if i % 3 == 2:
            print("+" + "---+"*9)
        else:
            print("+" + "   +"*9)


def create_grid(solution):
    grid = [[0 for _ in range(9)] for _ in range(9)]
    for s in solution:
        if s > 0:
            tmp = str(s)
            row = int(tmp[0]) - 1
            col = int(tmp[1]) - 1
            num = int(tmp[2])
            grid[row][col] = num
    return grid
