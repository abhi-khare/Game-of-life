"""
ToDos
- improve variable and function name
- simplify if there is a scope
- add comments
- functionality to reset the grid
- add functionality to resume and pause simulation
- add functionality to perform iteration 1 step at a time
- Chose better color scheme
"""

import pygame
import sys
from grid import GameGrid

pygame.init()
# params
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
RED = (250, 10, 10)
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
SCREEN.fill(BLACK)
SIMULATION = False
BLOCKSIZE = 10
ALIVE, DEAD = 1, 0
# grid object
grid = GameGrid(grid_height=int(WINDOW_HEIGHT / BLOCKSIZE),
                grid_width=int((WINDOW_WIDTH - 100) / BLOCKSIZE))


def draw_grid():
    for x in range(0, WINDOW_WIDTH - 100, BLOCKSIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCKSIZE):
            rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(SCREEN, GREY, rect, 1)


def fill_cell(yidx: int, xidx: int, STATUS: int):
    rect = pygame.Rect(xidx * BLOCKSIZE, yidx * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE)
    if STATUS == 1:
        pygame.draw.rect(SCREEN, RED, rect, width=0)
    else:
        pygame.draw.rect(SCREEN, BLACK, rect, width=0)


def simulation_begin(pos):
    x_pos, y_pos = pos
    if x_pos > 710 and y_pos < 50:
        return True
    else:
        return False


while True:
    clicked_pos = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if pygame.mouse.get_pressed()[0]:
            clicked_pos = pygame.mouse.get_pos()

    if clicked_pos is not None:
        if simulation_begin(clicked_pos):
            SIMULATION = True
            continue

        if SIMULATION is False:
            x_pos, y_pos = clicked_pos
            # transform coordinates into array indices
            y_idx, x_idx = int(y_pos / BLOCKSIZE), int(x_pos / BLOCKSIZE)
            fill_cell(y_idx, x_idx, 1)
            grid.set_cell(y_idx, x_idx, ALIVE)

    if SIMULATION:
        grid.run_iteration()
        grid_arr = grid.get_grid()
        for yidx, yval in enumerate(grid_arr):
            for xidx, xval in enumerate(yval):
                fill_cell(yidx, xidx, grid_arr[yidx][xidx][1])
    draw_grid()
    pygame.display.update()
