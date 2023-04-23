import math

ROWS = 6
COLS = 7
SQUARE_SIZE = 100
WIDTH, HEIGHT, RADIUS = COLS * SQUARE_SIZE, (ROWS + 1) * SQUARE_SIZE, int(SQUARE_SIZE / 2 - 5)
COMPUTER_PIECE = 'X'
PLAYER_PIECE = 'O'
MAX_DEPTH = 5
TIME = 0.5
C = math.sqrt(2)

# RGB
SNOW        = (255, 250, 250) # background
STEELBLUE   = (70, 130, 180)  # computador
DEEPSKYBLUE = (0, 191, 255)   # jogador
LIGHTSTEEL  = (176, 196, 222) # tabuleiro
