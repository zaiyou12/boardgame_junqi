import pygame

from games.piece import Piece

from .constants import BLACK, HEIGHT, RED, ROWS, COLS, SQUARE_SIZE, WHITE, WIDTH


class Board:
    def __init__(self) -> None:
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    def draw_squares(self, win: pygame.Surface) -> None:
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(
                    win,
                    RED,
                    (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                )

    def move(self, piece: Piece, row: int, col: int) -> None:
        self.board[piece.row][piece.col], self.board[row][col] = (
            self.board[row][col],
            self.board[piece.row][piece.col],
        )
        piece.move(row, col)

    def get_piece(self, row: int, col: int) -> Piece:
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row == 0:
                    self.board[row].append(Piece(row, col, WHITE))
                elif row == ROWS - 1:
                    self.board[row].append(Piece(row, col, RED))
                else:
                    self.board[row].append(0)

    def draw(self, win: pygame.surface, font: pygame.font.Font) -> None:
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win, font)
