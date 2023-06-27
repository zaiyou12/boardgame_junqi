import pygame

from games.board import Board
from games.constants import HEIGHT, WINDOW_WIDTH


FPS = 60

pygame.display.set_caption("Jun Qi")
pygame.font.init()

WIN = pygame.display.set_mode((WINDOW_WIDTH, HEIGHT))
FONT = pygame.font.SysFont(None, 30)


def main() -> None:
    run = True
    clock = pygame.time.Clock()
    board = Board()

    piece = board.get_piece(0, 1)
    board.move(piece, 4, 3)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw(WIN, FONT)
        pygame.display.update()
    pygame.quit()


main()
