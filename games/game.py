import pygame
from games.board import Board

from games.constants import (
    AVAILABLE_MOVE_TOKEN_RADIUS,
    BLUE,
    GREY,
    RED,
    COLS,
    SQUARE_SIZE,
    WHITE,
)
from games.utils import calc_pos


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

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = set()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.valid_moves.clear()
                self.select(row, col)
            return True
        else:
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True
        return False

    def _move(self, row, col):
        if self.selected and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.change_turn()
        else:
            return False
        return True

    def draw_cur_game_info(self, win: pygame.surface, font: pygame.font.Font):
        cur_player = 'RED' if self.turn == RED else 'WHITE'
        cur_player_text = font.render(f'Turn: {cur_player}', True, GREY)
        win.blit(cur_player_text, (COLS * SQUARE_SIZE + 5, 5))

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(
                self.win,
                BLUE,
                calc_pos(row, col),
                AVAILABLE_MOVE_TOKEN_RADIUS,
            )

    def change_turn(self):
        self.selected = None
        self.valid_moves.clear()
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED
