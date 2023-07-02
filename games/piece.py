from typing import Literal
import pygame

from games.utils import grid_to_pos
from .constants import GREY, PIECE_OUTLINE, PIECE_PADDING, SQUARE_SIZE


class Piece:
    def __init__(
        self,
        grid: tuple[int, int],
        color: tuple[Literal[255], Literal[255], Literal[255]],
        value: int = 0,
    ) -> None:
        self.grid = grid
        self.value = value
        self.color = color

    def draw(self, win: pygame.Surface, font: pygame.font.Font) -> None:
        radius = SQUARE_SIZE // 2 - PIECE_PADDING
        pygame.draw.circle(win, GREY, self.xy, radius + PIECE_OUTLINE)
        pygame.draw.circle(win, self.color, self.xy, radius)

        text = font.render(str(self.value), True, GREY)
        win.blit(
            text,
            (self.xy[0] - text.get_width() // 2, self.xy[1] - text.get_height() // 2),
        )

    def move(self, grid: tuple[int, int]) -> None:
        self.grid = grid

    @property
    def xy(self):
        return grid_to_pos(self.grid)

    def __repr__(self) -> str:
        return "Piece " + str(self.color)
