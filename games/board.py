import random
import pygame

from games.piece import Piece
from games.utils import is_grid_out_of_range

from .constants import (
    BLACK,
    DARK_BROWN,
    LIGHT_BROWN,
    PLAYER_1,
    ROWS,
    COLS,
    SQUARE_SIZE,
    WHITE,
)


class Board:
    EMPTY = 0

    def __init__(self) -> None:
        self.board = []
        self.selected_piece = None
        self.player_1_left = self.player_2_left = COLS
        self.create_board()
        self.create_pieces()

    def create_board(self):
        self.board = [[self.EMPTY for _ in range(COLS)] for _ in range(ROWS)]

    def create_pieces(self):
        for idx, value in enumerate(random.sample(range(1, COLS + 1), COLS)):
            self.board[0][idx] = Piece((0, idx), WHITE, value)
        for idx, value in enumerate(random.sample(range(1, COLS + 1), COLS)):
            self.board[ROWS - 1][idx] = Piece((ROWS - 1, idx), BLACK, value)

    def draw(self, win: pygame.surface, font: pygame.font.Font) -> None:
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win, font)

    def draw_squares(self, win: pygame.Surface) -> None:
        win.fill(LIGHT_BROWN)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(
                    win,
                    DARK_BROWN,
                    (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                )

    def move(self, piece: Piece, grid: tuple[int, int]) -> None:
        target = self.board[grid[0]][grid[1]]
        if target == self.EMPTY:
            self._move(piece, grid)
        elif piece.value >= target.value:
            self._move(piece, grid)
            self._update_left_piece(piece.color)
        else:
            self._update_left_piece(target.color)
            self.board[piece.grid[0]][piece.grid[1]] = self.EMPTY

    def _move(self, piece: Piece, grid: tuple[int, int]) -> None:
        self.board[grid[0]][grid[1]] = piece
        self.board[piece.grid[0]][piece.grid[1]] = self.EMPTY
        piece.move(grid)

    def _update_left_piece(self, win_color) -> None:
        if win_color == PLAYER_1:
            self.player_2_left -= 1
        else:
            self.player_1_left -= 1

    def get_piece(self, grid: tuple[int, int]) -> Piece:
        if is_grid_out_of_range(grid):
            return self.EMPTY
        return self.board[grid[0]][grid[1]]

    def get_valid_moves(self, piece: Piece) -> set:
        moves = set()
        direction = 1 if piece.color == WHITE else -1
        moves.update(self._traverse(piece, (direction, -1)))
        moves.update(self._traverse(piece, (direction, 0)))
        moves.update(self._traverse(piece, (direction, 1)))
        return moves

    def _traverse(
        self,
        piece: Piece,
        direction: tuple[int, int],
    ):
        moves = set()
        target_grid = (piece.grid[0] + direction[0], piece.grid[1] + direction[1])
        if is_grid_out_of_range(target_grid):
            return moves

        target = self.get_piece(target_grid)
        if target == self.EMPTY:
            moves.add(target_grid)
            return moves
        elif target.color == piece.color:
            return moves
        else:
            moves.add(target_grid)
            return moves
