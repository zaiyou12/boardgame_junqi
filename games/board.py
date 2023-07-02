from typing import Literal
import pygame

from games.piece import Piece
from games.utils import is_grid_out_of_range

from .constants import BLACK, RED, ROWS, COLS, SQUARE_SIZE, WHITE


class Board:
    EMPTY = 0

    def __init__(self) -> None:
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = COLS
        self.create_board()

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row == 0:
                    self.board[row].append(Piece(grid=(row, col), color=WHITE))
                elif row == ROWS - 1:
                    self.board[row].append(Piece(grid=(row, col), color=RED))
                else:
                    self.board[row].append(self.EMPTY)

    def draw(self, win: pygame.surface, font: pygame.font.Font) -> None:
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win, font)

    def draw_squares(self, win: pygame.Surface) -> None:
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(
                    win,
                    RED,
                    (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                )

    def move(self, piece: Piece, grid: tuple[int, int]) -> None:
        self.board[grid[0]][grid[1]] = piece
        self.board[piece.grid[0]][piece.grid[1]] = self.EMPTY
        piece.move(grid)

    def get_piece(self, grid: tuple[int, int]) -> Piece:
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
