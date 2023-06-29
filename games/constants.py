import pygame

ROWS, COLS = 5, 9
WIDTH, HEIGHT = COLS * 100, ROWS * 100
WINDOW_WIDTH = WIDTH + 400
SQUARE_SIZE = WIDTH // max(ROWS, COLS)

# rgb
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)

# size
AVAILABLE_MOVE_TOKEN_RADIUS = 15
