"""
TODO:
better code for handling list and indexes
"""

import pygame
import sys
from grid import GameGrid
from configurations import set_pattern
from arguments import arguments

# arguments and definitions
args = arguments()
WINDOW_WIDTH, WINDOW_HEIGHT = args.ww, args.wh
BLOCKSIZE = args.bs
BLACK = (0, 0, 0)
WHITE = (250, 250, 250)
GREY = (100, 100, 100)
GREEN = (34, 200, 34)
SIMULATION = False
ALIVE, DEAD = 1, 0

# Pygame initialisation
pygame.init()
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
SCREEN.fill(BLACK)
FPS = args.fps  # frames per second setting
fpsClock = pygame.time.Clock()


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


def fill_grid(grid_array: list) -> None:
    """
    This function loops through the grid_arr and call the fill_Cell
    function to fill individual cell on screen
    :param grid_array: List of list containing a tuple that stores backend grid information
    :return: None
    """
    for yidx, row in enumerate(grid_array):
        for xidx, col in enumerate(row):
            fill_cell(yidx, xidx, grid_array[yidx][xidx][0])


def draw_grid(grid_array) -> None:
    """
    This function draws grid on the screen by drawing rectangle of
    size - BLOCKSIZE in sequence.
    :return: None
    """
    fill_grid(grid_array)
    for x in range(0, WINDOW_WIDTH, BLOCKSIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCKSIZE):
            rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(SCREEN, GREY, rect, width=1)


# grid object
grid = GameGrid(grid_height=int(WINDOW_HEIGHT / BLOCKSIZE),
                grid_width=int(WINDOW_WIDTH / BLOCKSIZE))

while True:
    # capturing events
    for event in pygame.event.get():

        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            sys.exit()

        if pygame.mouse.get_pressed()[0]:
            x_pix_cor, y_pix_cor = pygame.mouse.get_pos()  # fetch mouse position if clicked
            y_idx, x_idx = int(y_pix_cor / BLOCKSIZE), int(x_pix_cor / BLOCKSIZE)
            pos = [(y_idx, x_idx)]
            grid.set_cell(pos, ALIVE)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                grid.reset_grid()  # reset the backend grid
                SIMULATION = False  # set simulation to False and allow setting cells
            if event.key == pygame.K_s:
                SIMULATION = True  # This disables setting cells on the screen
            if event.key == pygame.K_d:
                SIMULATION = False  # This enables setting cells on the screen
            if event.key == pygame.K_KP0:
                grid = set_pattern(grid, 'glider')
            if event.key == pygame.K_KP1:
                grid = set_pattern(grid, 'pentomino')

    if SIMULATION:
        grid.run_iteration()

    grid_arr = grid.get_grid()  # fetch the grid array
    draw_grid(grid_arr)
    pygame.display.update()
    fpsClock.tick(FPS)
