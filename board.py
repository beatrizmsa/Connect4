# ADICONAR INSTALAR PYGAME AO README
import pygame
import sys

# Define as constantes do jogo
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARE_SIZE = 100
WIDTH = COLUMN_COUNT * SQUARE_SIZE
HEIGHT = (ROW_COUNT + 1) * SQUARE_SIZE

# Define as cores do jogo
PURPLE = (195, 180, 220)
WHITE = (255, 255, 255)

# Inicializa o Pygame
pygame.init()

# Cria a janela do jogo
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define o título da janela do jogo
pygame.display.set_caption('4 em Linha')

# Desenha o tabuleiro do jogo
def draw_board():
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, PURPLE, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, WHITE, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), int(r*SQUARE_SIZE+SQUARE_SIZE+SQUARE_SIZE/2)), int(SQUARE_SIZE/2 - 5))

# Loop principal do jogo
while True:
    # Verifica se o jogo foi encerrado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Desenha o tabuleiro do jogo
    draw_board()

    # Atualiza a tela do jogo
    pygame.display.update()
