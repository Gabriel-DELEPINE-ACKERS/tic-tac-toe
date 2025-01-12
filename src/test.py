from main import create_grid, place_piece, verify_win


def test_create_grid():
    grid = create_grid(3, 3)
    assert len(grid) == 3
    assert all(len(row) == 3 for row in grid)
    assert all(cell == 0 for row in grid for cell in row)


def test_place_piece():
    grid = create_grid(3, 3)
    assert place_piece(grid, 1, 0, 1) is True
    assert grid[0][1] == 1
    assert place_piece(grid, 2, 0, 1) is False
    assert place_piece(grid, 2, 4, 1) is False


def test_verify_win():
    row_win = [[1, 1, 1], [0, 2, 0], [0, 0, 0]]
    assert verify_win(row_win) == 1

    col_win = [[1, 0, 0], [1, 2, 0], [1, 0, 0]]
    assert verify_win(col_win) == 1

    diag_win = [[2, 0, 0], [1, 2, 0], [1, 0, 2]]
    assert verify_win(diag_win) == 2

    no_win = [[2, 0, 0], [1, 1, 0], [1, 0, 2]]
    assert verify_win(no_win) == 0


test_create_grid()
test_place_piece()
test_verify_win()
