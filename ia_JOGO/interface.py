import pygame
import random
import sys
import math
from board1 import *
from strategies import minimax
from constanc import WIDTH,HEIGHT, RED, SQUARE_SIZE, RADIUS, WHITE, ROWS

# FPS
FPS = 60
pygame.init()
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
FRONT = pygame.font.SysFont("monospace",55)
pygame.display.set_caption('Connect 4')

# nossa main
def creat_board():
    board = [[" "," "," "," "," "," "],
             [" "," "," "," "," "," "],
             [" "," "," "," "," "," "],
             [" "," "," "," "," "," "],
             [" "," "," "," "," "," "],
             [" "," "," "," "," "," "],
             [" "," "," "," "," "," "]]
    return board

def mouse_motion(win, event, turn):
    pygame.draw.rect(win, WHITE, (0,0, WIDTH, SQUARE_SIZE))
    posx = event.pos[0]
    if turn == PLAYER_PIECE:
        pygame.draw.circle(win, RED, (posx, int(SQUARE_SIZE/2)), RADIUS)
    else:
        pygame.draw.circle(win, BLACK, (posx, int(SQUARE_SIZE/2)), RADIUS)

def humam_output(event,label, board):
    posx = event.pos[0]
    col = int(math.floor(posx/SQUARE_SIZE))
    row = board.count_pieces(col)
    if row != ROWS:
        board.board[col][row] = board.turn
        pygame.draw.circle(WIN, board.color, (posx, int(SQUARE_SIZE/2)), RADIUS)
        if board.checkWin(board.turn):
            label = FRONT.render(board.label,1,board.color)
            return False, label
    return True, label


def printBoard(board):
    top = '    1   2   3   4   5   6   7   '

    for j in range(0, ROWS):
        string = "   "
        j1 = 5 - j
        for i in range(0, COLS):
            if(board[i][j1] != " "):
                string += " " + board[i][j1] + "  "
            else:
                string += ' -  '
        print(string)
    print(top)
    print(" ")

def main(type, method):
    
    game = True
    clock = pygame.time.Clock()
    board = Board()
    board.board = creat_board()
    board.turn = random.choice(PLAYER_PIECE + COMPUTER_PIECE)
    board.set_label_color()
    label = None

    if method == '-' and type == '2-player':
        while game:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                if event.type == pygame.MOUSEMOTION:
                    mouse_motion(WIN,event,board.turn)
                    pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(WIN, WHITE, (0,0, WIDTH, SQUARE_SIZE))
                    if board.turn == PLAYER_PIECE:
                        game, label = humam_output(event,label,board)
                        print(board.utility())
                        printBoard(board.board)
                        board.turn = COMPUTER_PIECE
                        board.set_label_color()
                    else:
                        game, label = humam_output(event,label,board)
                        board.turn = PLAYER_PIECE
                        print(board.utility())
                        printBoard(board.board)
                        board.set_label_color()
            board.draw(WIN)
            pygame.display.update()
            if label != None :
                WIN.blit(label,(40,10))
                pygame.display.update()
            if game == False:
                pygame.time.wait(2500)
        pygame.quit()

    else:
        while game:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEMOTION:
                    mouse_motion(WIN,event,board.turn)
                    pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(WIN, WHITE, (0,0, WIDTH, SQUARE_SIZE))
                    if board.turn == PLAYER_PIECE:
                        game, label = humam_output(event,label,board)
                        pygame.display.update()
                        board.turn = COMPUTER_PIECE
                        board.set_label_color()
            
            if board.turn == COMPUTER_PIECE and game != False:
                _,col = minimax(board, 5, True)
                row = board.count_pieces(col)
                if row != ROWS:
                    board.board[col][row] = board.turn
                    if board.checkWin(board.turn):
                        label = FRONT.render(board.label,1,board.color)
                        game = False
                    board.turn = PLAYER_PIECE
                    board.set_label_color()
    
            board.draw(WIN)
            pygame.display.update()
            if label != None :
                WIN.blit(label,(40,10))
                pygame.display.update()
            if game == False:
                pygame.time.wait(2500)
        pygame.quit()

    
main(sys.argv[1], sys.argv[2])