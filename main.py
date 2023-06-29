import pygame

from games.board import Board
from games.constants import HEIGHT, RED, SQUARE_SIZE, WHITE, WINDOW_WIDTH
from games.game import Game


FPS = 60

pygame.display.set_caption("Jun Qi")
pygame.font.init()

WIN = pygame.display.set_mode((WINDOW_WIDTH, HEIGHT))
FONT = pygame.font.SysFont(None, 30)


def get_row_col_from_mouse(pos: tuple[int, int]):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main() -> None:
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN, FONT)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    pygame.quit()


main()
