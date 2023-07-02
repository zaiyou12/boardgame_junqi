import pygame
from games.constants import GREY, ROWS, COLS, SQUARE_SIZE


def xy_to_grid(pos: tuple[int, int]) -> tuple[int, int]:
    x, y = pos
    return y // SQUARE_SIZE, x // SQUARE_SIZE


def grid_to_pos(grid: tuple[int, int], center_align: bool = True) -> tuple[int, int]:
    row, col = grid
    modify = SQUARE_SIZE // 2 if center_align else 0
    return SQUARE_SIZE * col + modify, SQUARE_SIZE * row + modify


def is_grid_out_of_range(grid: tuple[int, int]) -> bool:
    return grid[0] < 0 or grid[0] >= ROWS or grid[1] < 0 or grid[1] >= COLS


def draw_text(
    text: str,
    xy: tuple[int, int],
    win: pygame.surface.Surface,
    font: pygame.font.Font,
    center_align: bool = False,
):
    text_surface = font.render(text, True, GREY)
    if center_align:
        xy = (
            xy[0] - text_surface.get_width() // 2,
            xy[1] - text_surface.get_height() // 2,
        )
    win.blit(text_surface, xy)
