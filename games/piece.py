from typing import Literal
import pygame

from games.utils import draw_text, grid_to_pos
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
        draw_text(str(self.value), self.xy, win, font, center_align=True)

    def move(self, grid: tuple[int, int]) -> None:
        self.grid = grid

    @property
    def xy(self):
        return grid_to_pos(self.grid)

    def __repr__(self) -> str:
        return "Piece " + str(self.color)
