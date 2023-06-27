from typing import Literal
import pygame
from .constants import GREY, RED, SQUARE_SIZE


class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(
        self, row: int, col: int, color: tuple[Literal[255], Literal[255], Literal[255]]
    ) -> None:
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        if self.color == RED:
            self.direction = -1
        else:
            self.direction = 1

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self) -> None:
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self) -> None:
        self.king = True

    def draw(self, win: pygame.Surface, font: pygame.font.Font) -> None:
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            text = font.render("K", True, GREY)
            win.blit(
                text, (self.x - text.get_width() // 2, self.y - text.get_height() // 2)
            )

    def move(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self) -> str:
        return "Piece " + str(self.color)
