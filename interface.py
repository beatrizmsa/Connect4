from constant import *
from board import *
from strategies import *
import math, contextlib, time
with contextlib.redirect_stdout(None):
    import pygame


def mouse_motion(wind, event, turn):
    pygame.draw.rect(wind, SNOW, (0, 0, WIDTH, SQUARE_SIZE))
    posx = event.pos[0]
    if turn == PLAYER_PIECE:
        pygame.draw.circle(wind, DEEPSKYBLUE, (posx, int(SQUARE_SIZE / 2)), RADIUS)
    else:
        pygame.draw.circle(wind, STEELBLUE, (posx, int(SQUARE_SIZE / 2)), RADIUS)


def humam_output(event, label, board, WINDOW, FONT):
    posx = event.pos[0]
    col = int(math.floor(posx / SQUARE_SIZE))
    row = board.count_pieces(col)
    if row < ROWS:
        board.board[col][row] = board.turn
        pygame.draw.circle(WINDOW, board.color, (posx, int(SQUARE_SIZE / 2)), RADIUS)
        if board.checkWin(board.turn):
            label = FONT.render(board.label, 1, board.color)
            return False, label, True
    else:
        return True, label, False
    return True, label, True


def main():
    print("Select the game mode you want:")
    print("1 - player VS player")
    print("2 - player VS computer")
    print()

    type = int(input())

    print()

    if(type != 1):
        print("Select the game method you want:")
        print("1 - minimax")
        print("2 - alphabeta")
        print("3 - monte carlo")
        print()

        method = int(input())
        print()

    # FPS
    FPS = 60
    pygame.init()
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    FONT = pygame.font.SysFont("arial", 50)
    pygame.display.set_caption('Connect 4')

    game = True
    clock = pygame.time.Clock()
    board = Board()
    label = None
    tie_message = "tie !"
    tie = FONT.render(tie_message, 1, LIGHTSTEEL)

    # playerVSplayer
    if type == 1:
        print("player VS player")
        while game:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEMOTION:
                    mouse_motion(WINDOW, event, board.turn)
                    pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(WINDOW, SNOW, (0, 0, WIDTH, SQUARE_SIZE))
                    if board.turn == PLAYER_PIECE:
                        game, label, play = humam_output(event, label, board, WINDOW, FONT)
                        if play:
                            board.printBoard()
                            board.set_turn()
                            board.moves += 1
                    else:
                        game, label, play= humam_output(event, label, board, WINDOW, FONT)
                        if play:
                            board.printBoard()
                            board.set_turn()
                            board.moves += 1

            board.draw(WINDOW)
            pygame.display.update()
            if label != None:
                WINDOW.blit(label, (40, 10))
                pygame.display.update()
            if board.moves == 42:
                game = False
                WINDOW.blit(tie, (40, 10))
                pygame.display.update()
            if game == False:
                if(board.moves < 42):
                    if(board.turn == PLAYER_PIECE):
                        board.turn = COMPUTER_PIECE
                    else:
                        board.turn = PLAYER_PIECE
                    print("Player ", board.turn, " wins !")
                else:
                    print("Tie !")
                pygame.time.wait(CLOSE_TIME)
        pygame.quit()

    elif type == 2 and method == 1:
        print("player VS computer -> minimax")
        while game:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEMOTION:
                    mouse_motion(WINDOW,event,board.turn)
                    pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(WINDOW, SNOW, (0, 0, WIDTH, SQUARE_SIZE))
                    if board.turn == PLAYER_PIECE:
                        game, label, play= humam_output(event, label, board, WINDOW,FONT)
                        if play:
                            board.printBoard()
                            board.draw(WINDOW)
                            pygame.display.update()
                            board.set_turn()
                            board.moves += 1

            if board.turn == COMPUTER_PIECE and game != False:
                _, cols ,_ = minimax(board, MAX_DEPTH, True)
                best_col = random.choice(cols)
                row = board.count_pieces(best_col)
                board.board[best_col][row] = board.turn
                if board.checkWin(board.turn):
                    label = FONT.render(board.label, 1, board.color)
                    game = False
                board.printBoard()
                board.set_turn()
                board.moves += 1
            
            board.draw(WINDOW)
            pygame.display.update()
            if label != None:
                WINDOW.blit(label, (40, 10))
                pygame.display.update()
            if board.moves == 42:
                game = False
                WINDOW.blit(tie, (40, 10))
                pygame.display.update()
            if game == False:
                if(board.moves < 42):
                    if(board.turn == PLAYER_PIECE):
                        board.turn = COMPUTER_PIECE
                    else:
                        board.turn = PLAYER_PIECE
                    print("Player ", board.turn, " wins !")
                else:
                    print("Tie !")
                print()
                end = time.time()
                print("nodes generated: ", board.visit)
                pygame.time.wait(CLOSE_TIME)
        pygame.quit()

    elif type == 2 and method == 2:
        print("player VS computer -> alphabeta")
        while game:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEMOTION:
                    mouse_motion(WINDOW, event, board.turn)
                    pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(WINDOW, SNOW, (0, 0, WIDTH, SQUARE_SIZE))
                    if board.turn == PLAYER_PIECE:
                        game, label, play = humam_output(event, label,board, WINDOW, FONT)
                        if play:
                            board.printBoard()
                            board.draw(WINDOW)
                            pygame.display.update()
                            board.set_turn()
                            board.moves += 1

            if board.turn == COMPUTER_PIECE and game != False:
                _, cols ,_ = alphabeta(board, MAX_DEPTH, -math.inf, math.inf, True)
                best_col = random.choice(cols)
                row = board.count_pieces(best_col)
                board.board[best_col][row] = board.turn
                if board.checkWin(board.turn):
                    label = FONT.render(board.label, 1, board.color)
                    game = False
                board.printBoard()
                board.set_turn()
                board.moves += 1

            board.draw(WINDOW)
            pygame.display.update()
            if label != None:
                WINDOW.blit(label, (40, 10))
                pygame.display.update()
            if board.moves == 42:
                game = False
                WINDOW.blit(tie, (40, 10))
                pygame.display.update()
            if game == False:
                if(board.moves < 42):
                    if(board.turn == PLAYER_PIECE):
                        board.turn = COMPUTER_PIECE
                    else:
                        board.turn = PLAYER_PIECE
                    print("Player ", board.turn, " wins !")
                else:
                    print("Tie !")
                print()
                print("nodes generated: ", board.visit)
                pygame.time.wait(CLOSE_TIME)
        pygame.quit()

    # implementação não esta correta
    elif type == 2 and method == 3:
        print("player VS computer -> montecarlo")
        while game:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEMOTION:
                    mouse_motion(WINDOW, event, board.turn)
                    pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(WINDOW, SNOW, (0, 0, WIDTH, SQUARE_SIZE))
                    if board.turn == PLAYER_PIECE:
                        posx = event.pos[0]
                        col = int(math.floor(posx / SQUARE_SIZE))
                        row = board.count_pieces(col)
                        if row < ROWS:
                            game, label, play = humam_output(event, label, board, WINDOW, FONT)
                            if play:
                                board.printBoard()
                                board.draw(WINDOW)
                                pygame.display.update()
                                board.turn = COMPUTER_PIECE
                                board.set_label_color()

            if board.turn == COMPUTER_PIECE and game != False:
                best_col = monte_carlos_tree_search(board, TIME)
                row = board.count_pieces(best_col)
                board.board[best_col][row] = board.turn
                if board.checkWin(board.turn):
                    label = FONT.render(board.label, 1, board.color)
                    game = False
                board.printBoard()
                board.turn = PLAYER_PIECE
                board.set_label_color()
            board.draw(WINDOW)
            pygame.display.update()
            if label != None:
                WINDOW.blit(label, (40, 10))
                pygame.display.update()
            if game == False:
                print()
                if(board.moves < 42):
                    if(board.turn == PLAYER_PIECE):
                        board.turn = COMPUTER_PIECE
                    else:
                        board.turn = PLAYER_PIECE
                    print("Player ", board.turn, " wins !")
                else:
                    print("Tie !")
                # print("nodes generated: ", board.visit)
                pygame.time.wait(CLOSE_TIME)
        pygame.quit()

main()
