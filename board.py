import contextlib

with contextlib.redirect_stdout(None):
    import pygame

from time import sleep
import auxFunctions
import strategies
import checkWin

PLAYER_PIECE = 'X'
COMPUTER_PIECE = 'O'
CURRENT_PLAYER = PLAYER_PIECE

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 600
CELL_SIZE = 100

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 225, 0)

def switch_player():
    global CURRENT_PLAYER
    if CURRENT_PLAYER == PLAYER_PIECE:
        CURRENT_PLAYER = COMPUTER_PIECE
    else:
        CURRENT_PLAYER = PLAYER_PIECE

def draw_board(board, screen):
    # Fill screen with white background
    screen.fill(WHITE)

    # Draw gridlines
    for i in range(8):
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_HEIGHT), 5)
    for i in range(7):
        pygame.draw.line(screen, BLACK, (0, (i + 1) * CELL_SIZE), (WINDOW_WIDTH, (i + 1) * CELL_SIZE), 5)

    # Draw game pieces
    for i in range(7):
        for j in range(6):
            if board[i][j] == 'X':
                pygame.draw.circle(screen, RED, (int((j + 0.5) * CELL_SIZE), int((i + 0.5) * CELL_SIZE)),
                                   int(CELL_SIZE * 0.4))
            elif board[i][j] == 'O':
                pygame.draw.circle(screen, YELLOW, (int((j + 0.5) * CELL_SIZE), int((i + 0.5) * CELL_SIZE)),
                                   int(CELL_SIZE * 0.4))


def handle_input(game, algorithm = None):
    pos = pygame.mouse.get_pos()
    column = pos[0] // CELL_SIZE
    game, flag = auxFunctions.move(game, column, CURRENT_PLAYER)
    if flag:
        if algorithm is not None and not checkWin.checkWin(game):
            auxFunctions.move(game, strategies.minimax(game, algorithm), COMPUTER_PIECE)
    return game

def game_over_screen(screen, winner):
    pygame.font.init()
    screen.fill(WHITE)

    font = pygame.font.SysFont("Arial", 50)

    if winner == "X":
        winner_text = font.render("Red wins!", True, RED)
    elif winner == "O":
        winner_text = font.render("Yellow wins!", True, YELLOW)
    else:
        winner_text = font.render("It's a tie!", True, BLACK)

    winner_text_rect = winner_text.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 3))
    screen.blit(winner_text, winner_text_rect)

    pygame.display.update()
    sleep(1.5)


def main(game, algorithm=None):
    flag = False
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Connect 4')

    while True:
        # print(game.get_turn())
        screen.fill(WHITE)
        draw_board(game, screen)
        pygame.display.update()

        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game=handle_input(game, algorithm)

        if flag:
            sleep(2.5)
            game_over_screen(screen, checkWin.checkWin())
            exit()

        if checkWin.checkWin(CURRENT_PLAYER, game):
            flag = True
