ALIVE = 1
DEAD = 0


class GameGrid:

    def __init__(self, grid_height: int, grid_width: int) -> None:
        self.grid = [[[0, 0] for x in range(grid_width)]
                     for y in range(grid_height)]
        self.grid_height = grid_height
        self.grid_width = grid_width

    def set_cell(self, y_idx: int, x_idx: int, status: int, old: bool = True) -> None:
        """
        This function sets the status of the cell (old/new)
        :param y_idx: y index of the cell
        :param x_idx: x index of the cell
        :param status: Alive/Dead
        :param old: Whether to update old state or new state
        :return: None
        """
        if old:
            self.grid[y_idx][x_idx][0] = status
        else:
            self.grid[y_idx][x_idx][1] = status

    def get_grid(self) -> None:
        return self.grid

    def reset_grid(self) -> None:
        self.grid = [[[0, 0] for x in range(self.grid_width)]
                     for y in range(self.grid_height)]

    def get_neighbour_count(self, y_idx, x_idx):
        """
        For a cell with index (y_idx, x_idx), it returns the number of ALIVE
        neighbours
        :param y_idx: y index of the cell
        :param x_idx: x index of the cel
        :return: None
        """
        num_neighbour = 0
        if x_idx - 1 >= 0:
            num_neighbour += self.grid[y_idx][x_idx - 1][0]
        if y_idx - 1 >= 0:
            num_neighbour += self.grid[y_idx - 1][x_idx][0]
        if x_idx + 1 < self.grid_width:
            num_neighbour += self.grid[y_idx][x_idx + 1][0]
        if y_idx + 1 < self.grid_height:
            num_neighbour += self.grid[y_idx + 1][x_idx][0]
        if y_idx - 1 >= 0 and x_idx - 1 >= 0:
            num_neighbour += self.grid[y_idx - 1][x_idx - 1][0]
        if y_idx + 1 < self.grid_height and x_idx + 1 < self.grid_width:
            num_neighbour += self.grid[y_idx + 1][x_idx + 1][0]
        if y_idx + 1 < self.grid_height and x_idx - 1 >= 0:
            num_neighbour += self.grid[y_idx + 1][x_idx - 1][0]
        if y_idx - 1 >= 0 and x_idx + 1 < self.grid_width:
            num_neighbour += self.grid[y_idx - 1][x_idx + 1][0]

        return num_neighbour

    def run_iteration(self) -> None:
        """
        This functions performs iteration based on the Rules of Convey's Game of life.
        To summarise:
        1) If a cell is alive and it has less than 3 alive neighbours, it dies due to loneliness.
        2) If a cell is alive and it has more than 3 alive neighbours, it dies due to over population.
        3) If a cell is alive and it has exactly 3 alive neighbours, it continues to live.
        4) If a cell is dead and it has exactly 3 alive neighbours, it becomes alive due to reproduction ;).

        More information at : https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

        :return: None
        """
        for y_idx in range(self.grid_height):
            for x_idx in range(self.grid_width):
                if self.grid[y_idx][x_idx][0] == ALIVE:
                    num_neighbour = self.get_neighbour_count(y_idx, x_idx)
                    if num_neighbour < 2 or num_neighbour > 3:
                        self.set_cell(y_idx, x_idx, DEAD, False)
                    else:
                        self.set_cell(y_idx, x_idx, ALIVE, False)
                else:
                    num_neighbour = self.get_neighbour_count(y_idx, x_idx)
                    if num_neighbour == 3:
                        self.set_cell(y_idx, x_idx, ALIVE, False)

        for y_idx in range(self.grid_height):
            for x_idx in range(self.grid_width):
                self.set_cell(y_idx, x_idx, self.grid[y_idx][x_idx][1], True)
