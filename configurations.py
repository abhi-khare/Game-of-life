ALIVE = 1

# configuration stores the offset of each point in grid with respect to the
# center of the grid
configurations = {
    'glider': [(0, 0), (0, 1), (0, 2), (-1, 2), (-2, 1)],
    'pentomino': [(0, 0), (1, 0), (2, 0), (0, 1), (1, -1)]
}


def set_pattern(grid, pattern_id):
    mid_x = int(grid.grid_width / 2)
    mid_y = int(grid.grid_height / 2)
    pos = [(mid_y + ydiff, mid_x + xdiff) for ydiff, xdiff in configurations[pattern_id]]
    grid.set_cell(pos, ALIVE)

    return grid
