ROWS, COLS = 7, 7
WIDTH, HEIGHT = COLS * 100, ROWS * 100
WINDOW_WIDTH = WIDTH + 400
SQUARE_SIZE = WIDTH // max(ROWS, COLS)

# rgb
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
LIGHT_BROWN = (242, 225, 195)
DARK_BROWN = (195, 160, 130)
GREEN = (109, 204, 102)

# color
PLAYER_1 = BLACK
PLAYER_2 = WHITE
TOKEN = GREEN

# size
TOKEN_RADIUS = 20
PIECE_PADDING = 15
PIECE_OUTLINE = 2

# game info
GAME_DESCRIPTION = [
    "Game rules",
    "",
    "1. Catch opponent's 2 to win!",
    "2. 2 cannot move",
    "3. Big number wins small number",
    "4. But 1 wins over biggest number",
    "5. If the numbers are equal,",
    "the attacker wins",
]
