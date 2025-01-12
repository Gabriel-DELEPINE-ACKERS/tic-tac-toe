from main import create_grid, place_piece


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


test_create_grid()
test_place_piece()
