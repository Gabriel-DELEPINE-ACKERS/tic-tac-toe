from main import create_grid


def test_create_grid():
    grid = create_grid(3, 3)
    assert len(grid) == 3
    assert all(len(row) == 3 for row in grid)
    assert all(cell == 0 for row in grid for cell in row)


test_create_grid()
