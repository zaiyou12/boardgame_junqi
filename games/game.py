import pygame
from games.board import Board

from games.constants import (
    GREY,
    TOKEN_RADIUS,
    TOKEN,
    GAME_DESCRIPTION,
    HEIGHT,
    PLAYER_1,
    PLAYER_2,
    COLS,
    SQUARE_SIZE,
)
from games.utils import draw_text, grid_to_pos


class Game:
    def __init__(self, win: pygame.surface.Surface, font: pygame.font.Font) -> None:
        self._init()
        self.win = win
        self.font = font

    def update(self) -> None:
        self.board.draw(self.win, self.font)
        self.draw_cur_game_info(self.win, self.font)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def reset(self) -> None:
        self._init()

    def _init(self) -> None:
        self.board = Board()
        self.turn = PLAYER_1
        self.selected = None
        self.valid_moves = set()

    def select(self, grid: tuple[int, int]) -> bool:
        if self.selected:
            result = self._move(grid)
            if not result:
                self.selected = None
                self.valid_moves.clear()
                self.select(grid)
            return True
        else:
            piece = self.board.get_piece(grid)
            if piece != 0 and piece.color == self.turn and piece.value != 2:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True
        return False

    def _move(self, grid: tuple[int, int]) -> bool:
        if self.selected and grid in self.valid_moves:
            self.board.move(self.selected, grid)
            self.change_turn()
        else:
            return False
        return True

    def draw_cur_game_info(self, win: pygame.surface.Surface, font: pygame.font.Font):
        x = COLS * SQUARE_SIZE
        pygame.draw.line(win, GREY, (x, 0), (x, HEIGHT))

        x += 20
        turn = "Player 1" if self.turn == PLAYER_1 else "Player 2"
        draw_text(f"Turn: {turn}", (x, 20), win, font)
        draw_text(f"Player 1 left: {self.board.player_1_left}", (x, 70), win, font)
        draw_text(f"Player 2 left: {self.board.player_2_left}", (x, 95), win, font)

        base_y = HEIGHT // 2
        for idx, text in enumerate(GAME_DESCRIPTION):
            draw_text(text, (x, base_y + idx * 25), win, font)

    def draw_valid_moves(self, moves):
        for move in moves:
            grid = move
            pygame.draw.circle(
                self.win,
                TOKEN,
                grid_to_pos(grid),
                TOKEN_RADIUS,
            )

    def change_turn(self):
        self.selected = None
        self.valid_moves.clear()
        if self.turn == PLAYER_1:
            self.turn = PLAYER_2
        else:
            self.turn = PLAYER_1
