from games.constants import SQUARE_SIZE


def calc_pos(row, col):
    half = SQUARE_SIZE // 2
    return SQUARE_SIZE * col + half, SQUARE_SIZE * row + half
