# 0 - empty, 1 - player1 , 2 - player2
def create_grid(row, col):
    grid = []
    for i in range(row):
        grid.append([0] * col)
    return grid


grid = create_grid(3, 3)
print(grid)


def is_legal_play(grid, player, row, col):
    return grid[row][col] == 0


def is_in_grid(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def place_piece(grid, player, row, col):
    if not is_in_grid(grid, row, col) or not is_legal_play(grid, player, row, col):
        return False
    grid[row][col] = player
    return True


print(place_piece(grid, 1, 0, 1))
print(grid)
print(place_piece(grid, 2, 0, 1))
print(grid)
