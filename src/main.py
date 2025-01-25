# 0 - empty, 1 - player1 , 2 - player2
def create_grid(row, col):
    grid = []
    for i in range(row):
        grid.append([0] * col)
    return grid


def is_legal_play(grid, player, row, col):
    if grid[row][col] == 0:
        return True
    else:
        return False


def is_in_grid(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def place_piece(grid, player, row, col):
    if not is_in_grid(grid, row, col) or not is_legal_play(grid, player, row, col):
        return False
    grid[row][col] = player
    return True

def verify_win(grid):
    for i in range(len(grid)):
        row = grid[i]
        print(row)
        if row[0] == row[1] == row[2] != 0:
            return row[0]

    for i in range(len(grid[0])):
        col = [grid[0][i], grid[1][i], grid[2][i]]

        if col[0] == col[1] == col[2] != 0:
            return col[0]

    diag1 = [grid[0][0], grid[1][1], grid[2][2]]
    if diag1[0] == diag1[1] == diag1[2] != 0:
        return diag1[0]

    diag2 = [grid[0][2], grid[1][1], grid[2][0]]
    if diag2[0] == diag2[1] == diag2[2] != 0:
        return diag2[0]

    return 0
