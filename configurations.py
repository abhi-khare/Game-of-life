ALIVE = 1


def set_pattern(grid, pattern_id):
    mid_x, mid_y = int(grid.grid_width / 2), int(grid.grid_height / 2)

    if pattern_id == 'glider':
        pos = [(mid_y, mid_x),
               (mid_y, mid_x + 1),
               (mid_y, mid_x + 2),
               (mid_y - 1, mid_x + 2),
               (mid_y - 2, mid_x + 1)]
        grid.set_cell(pos, ALIVE)

    if pattern_id == 'pentomino':
        pos = [(mid_y, mid_x),
               (mid_y + 1, mid_x),
               (mid_y + 2, mid_x),
               (mid_y, mid_x + 1),
               (mid_y+1, mid_x-1)]
        grid.set_cell(pos, ALIVE)

    if pattern_id == 'pentomino':
        pos = [(mid_y, mid_x),
               (mid_y + 1, mid_x),
               (mid_y + 2, mid_x),
               (mid_y, mid_x + 1),
               (mid_y + 1, mid_x - 1)]
        grid.set_cell(pos, ALIVE)

    return grid
