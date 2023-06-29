import pygame

from games.piece import Piece

from .constants import BLACK, RED, ROWS, COLS, SQUARE_SIZE, WHITE


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
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(
                    win,
                    RED,
                    (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
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

    def get_valid_moves(self, piece):
        moves = set()

        row = piece.row
        col = piece.col
        if piece.color == RED:
            start = row - 1
            stop = max(row - 3, -1)
            direction = -1
        else:
            start = row + 1
            stop = min(row + 3, ROWS)
            direction = 1
        left = piece.col - 1
        right = piece.col + 1

        moves.update(self._traverse_left(start, stop, direction, piece.color, left))
        moves.update(self._traverse_forward(start, stop, direction, piece.color, col))
        moves.update(self._traverse_right(start, stop, direction, piece.color, right))
        return moves

    def _traverse_left(self, start, stop, step, color, left):
        moves = set()
        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.get_piece(r, left)
            if current == 0:
                moves.add((r, left))
                break
            elif current.color == color:
                break
            else:
                moves.add((r, left))
                break
            left -= 1
        return moves

    def _traverse_forward(self, start, stop, step, color, col):
        moves = set()
        for r in range(start, stop, step):
            current = self.get_piece(r, col)
            if current == 0:
                moves.add((r, col))
                break
            elif current.color == color:
                break
            else:
                moves.add((r, col))
                break
        return moves
        pass

    def _traverse_right(self, start, stop, step, color, right):
        moves = set()
        for r in range(start, stop, step):
            if right >= COLS:
                break
            current = self.get_piece(r, right)
            if current == 0:
                moves.add((r, right))
                break
            elif current.color == color:
                break
            else:
                moves.add((r, right))
                break
            right += 1
        return moves
