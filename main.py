import pygame

from games.constants import HEIGHT, SQUARE_SIZE, WINDOW_WIDTH
from games.game import Game
from games.utils import xy_to_grid


FPS = 60

pygame.display.set_caption("Jun Qi")
pygame.font.init()

WIN = pygame.display.set_mode((WINDOW_WIDTH, HEIGHT))
FONT = pygame.font.SysFont(None, 30)


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
                game.select(xy_to_grid(pos))

        game.update()
    pygame.quit()


main()
