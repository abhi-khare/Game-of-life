"""
ToDos
- improve variable and function name
- add functionality to perform iteration 1 step at a time
"""

import pygame
import sys
from grid import GameGrid

# params
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 800
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
GREEN = (34, 200, 34)
SIMULATION = False
BLOCKSIZE = 10
ALIVE, DEAD = 1, 0

# Pygame initialisation
pygame.init()
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
SCREEN.fill(BLACK)

# grid object
grid = GameGrid(grid_height=int(WINDOW_HEIGHT / BLOCKSIZE),
                grid_width=int(WINDOW_WIDTH / BLOCKSIZE))


def draw_grid() -> None:
    """
    This function draws grid on the screen by drawing rectangle of
    size - BLOCKSIZE in sequence. This can be improved by drawing parallel
    lines.[ToDo]
    :return: None
    """
    for x in range(0, WINDOW_WIDTH, BLOCKSIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCKSIZE):
            rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(SCREEN, GREY, rect, 1)


def fill_cell(yidx: int, xidx: int, status: int) -> None:
    """
    This function fills the (xidx,yidx) cell on the screen
    :param yidx: y index of the cell, where index of topmost cell is 0
    :param xidx: x index of the cell, where index of leftmost cell is 0
    :param status: whether the cell is alive or not
    :return: None
    """
    rect = pygame.Rect(xidx * BLOCKSIZE, yidx * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE)
    if status == 1:
        pygame.draw.rect(SCREEN, GREEN, rect, width=0)
    else:
        pygame.draw.rect(SCREEN, BLACK, rect, width=0)


def fill_grid(grid_arr: list) -> None:
    """
    This function loops through the grid_arr and call the fill_Cell
    function to fill individual cell on screen
    :param grid_arr: List of list containing a tuple that stores backend grid information
    :return: None
    """
    for yidx, yval in enumerate(grid_arr):
        for xidx, xval in enumerate(yval):
            fill_cell(yidx, xidx, grid_arr[yidx][xidx][1])


while True:
    clicked_pos = None
    # capturing events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if pygame.mouse.get_pressed()[0]:
            clicked_pos = pygame.mouse.get_pos()  # fetch mouse position if clicked

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                grid.reset_grid()  # reset the backend grid
                grid_arr = grid.get_grid()  # fetch the grid array
                fill_grid(grid_arr)  # call the fill_grid function to wipe the grid
                SIMULATION = False  # set simulation to False and allow setting cells
            if event.key == pygame.K_s:
                SIMULATION = True  # This disables setting cells on the screen
            if event.key == pygame.K_d:
                SIMULATION = False # This enables setting cells on the screen

    if clicked_pos is not None and SIMULATION is False:
        x_pos, y_pos = clicked_pos
        # transform coordinates into array indices
        y_idx, x_idx = int(y_pos / BLOCKSIZE), int(x_pos / BLOCKSIZE)
        fill_cell(y_idx, x_idx, 1)
        grid.set_cell(y_idx, x_idx, ALIVE)

    if SIMULATION:
        grid.run_iteration()
        grid_arr = grid.get_grid()
        fill_grid(grid_arr)

    draw_grid()
    pygame.display.update()
