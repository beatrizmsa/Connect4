# colocar num ficheiro de constantes
ROWS, COLS = 6, 7
SQUARE_SIZE = 100
WIDTH,HEIGHT, RADIUS = COLS*SQUARE_SIZE,(ROWS+1)*SQUARE_SIZE, int(SQUARE_SIZE/2 -5)
COMPUTER_PIECE = 'X'   # computador no minimax queremos sempre o maximo, logo a nosso pontuaçao tem que ser positiva
PLAYER_PIECE = 'O'
MAX_DEPTH = 3

# RGB
STEELBLUE   = (70, 130, 180)
SNOW        = (255, 250, 250)
DEEPSKYBLUE = (0, 191, 255)
LIGHTSTEEL  = (176, 196, 222)
