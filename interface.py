from constant import *
from board import *
from strategies import *
import math, contextlib
with contextlib.redirect_stdout(None):
    import pygame

def mouse_motion(wind, event, turn):
    pygame.draw.rect(wind, SNOW, (0, 0, WIDTH, SQUARE_SIZE))
    posx = event.pos[0]
    if turn == PLAYER_PIECE:
        pygame.draw.circle(wind, DEEPSKYBLUE, (posx, int(SQUARE_SIZE / 2)), RADIUS)
    else:
        pygame.draw.circle(wind, LIGHTSTEEL, (posx, int(SQUARE_SIZE / 2)), RADIUS)

def humam_output(event, label, board, WINDOW, FONT):
    posx = event.pos[0]
    col = int(math.floor(posx / SQUARE_SIZE))
    row = board.count_pieces(col)
    if row < ROWS:
        board.board[col][row] = board.turn
        pygame.draw.circle(WINDOW, board.color, (posx, int(SQUARE_SIZE / 2)), RADIUS)
        if board.checkWin(board.turn):
            label = FONT.render(board.label, 1, board.color)
            return False, label
    else:
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(WINDOW, SNOW, (0, 0, WIDTH, SQUARE_SIZE))
            if board.turn == PLAYER_PIECE:
                game, label = humam_output(event, label, board, WINDOW, FONT)
                print(board.utility())
                board.printBoard()
                board.turn = COMPUTER_PIECE
                board.set_label_color()
    return True, label

def main():
    print("Select the game mode you want:")
    print("1 - player VS player")
    print("2 - player VS computer")
    # print("3 - computer VS computer")
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
                    game = False
                if event.type == pygame.MOUSEMOTION:
                    mouse_motion(WINDOW, event, board.turn)
                    pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(WINDOW, SNOW, (0, 0, WIDTH, SQUARE_SIZE))
                    if board.turn == PLAYER_PIECE:
                        game, label = humam_output(event, label, board, WINDOW, FONT)
                        print(board.utility())
                        board.printBoard()
                        board.turn = COMPUTER_PIECE
                        board.set_label_color()
                        board.moves += 1
                    else:
                        game, label = humam_output(event, label, board, WINDOW, FONT)
                        board.turn = PLAYER_PIECE
                        print(board.utility())
                        board.printBoard()
                        board.set_label_color()
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
                pygame.time.wait(10000)
        pygame.quit()

    elif type == 2 and method == 1:
        print("player VS computer -> minimax")
        while game:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                if event.type == pygame.MOUSEMOTION:
                    mouse_motion(WINDOW,event,board.turn)
                    pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(WINDOW, SNOW, (0, 0, WIDTH, SQUARE_SIZE))
                    if board.turn == PLAYER_PIECE:
                        posx = event.pos[0]
                        col = int(math.floor(posx / SQUARE_SIZE))
                        row = board.count_pieces(col)
                        if row < ROWS:
                            game, label = humam_output(event, label, board, WINDOW,FONT)
                            board.draw(WINDOW)
                            pygame.display.update()
                            board.turn = COMPUTER_PIECE
                            board.set_label_color()

            if board.turn == COMPUTER_PIECE and game != False:
                best_cost = -math.inf
                best_col = 0
                for(col, newboard) in board.successors(COMPUTER_PIECE):
                    cost = minimax(newboard, 3, False)
                    if cost > best_cost:
                        best_cost = cost
                        best_col = col
                row = board.count_pieces(best_col)
                board.board[best_col][row] = board.turn
                if board.checkWin(board.turn):
                    label = FONT.render(board.label, 1, board.color)
                    game = False
                board.turn = PLAYER_PIECE
                board.set_label_color()
            board.draw(WINDOW)
            pygame.display.update()
            if label != None:
                WINDOW.blit(label,(40, 10))
                pygame.display.update()
            if game == False:
                pygame.time.wait(10000)
        pygame.quit()

    # elif type == 3 and method == 1:
    #     print('computer VS computer -> minimax')
    #     while game:
    #         clock.tick(FPS)
    #         if board.turn == PLAYER_PIECE and game != False:
    #             best_cost = +math.inf
    #             best_col = 0
    #             for(col, newboard) in board.successors(PLAYER_PIECE):
    #                 cost = minimax(newboard, 3,True)
    #                 if cost < best_cost:
    #                     best_cost = cost
    #                     best_col = col
    #             row = board.count_pieces(best_col)
    #             board.board[best_col][row] = board.turn
    #             if board.checkWin(board.turn):
    #                 label = FONT.render(board.label,1,board.color)
    #                 game = False
    #             board.turn = COMPUTER_PIECE
    #             board.set_label_color()

    #         pygame.time.wait(2500)

    #         if board.turn == COMPUTER_PIECE and game != False:
    #             best_cost = -math.inf
    #             best_col = 0
    #             for(col, newboard) in board.successors(COMPUTER_PIECE):
    #                 cost = minimax(newboard, 3,False)
    #                 if cost > best_cost:
    #                     best_cost = cost
    #                     best_col = col
    #             row = board.count_pieces(best_col)
    #             board.board[best_col][row] = board.turn
    #             if board.checkWin(board.turn):
    #                 label = FONT.render(board.label,1,board.color)
    #                 game = False
    #             board.turn = PLAYER_PIECE
    #             board.set_label_color()

    #         board.draw(WINDOW)
    #         pygame.display.update()
    #         if label != None:
    #             WINDOW.blit(label,(40, 10))
    #             pygame.display.update()
    #         if game == False:
    #             pygame.time.wait(10000)
    #     pygame.quit()

    elif type == 2 and method == 2:
        print("player VS computer -> alphabeta")
        while game:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                if event.type == pygame.MOUSEMOTION:
                    mouse_motion(WINDOW, event, board.turn)
                    pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(WINDOW, SNOW, (0, 0, WIDTH, SQUARE_SIZE))
                    if board.turn == PLAYER_PIECE:
                        posx = event.pos[0]
                        col = int(math.floor(posx/SQUARE_SIZE))
                        row = board.count_pieces(col)
                        if row < ROWS:
                            game, label = humam_output(event, label,board, WINDOW, FONT)
                            board.draw(WINDOW)
                            pygame.display.update()
                            board.turn = COMPUTER_PIECE
                            board.set_label_color()

            if board.turn == COMPUTER_PIECE and game != False:
                best_cost = -math.inf
                best_col = 0
                for(col, newboard) in board.successors(COMPUTER_PIECE):
                    cost = alphabeta(newboard, 3, -math.inf, math.inf, False)
                    if cost > best_cost:
                        best_cost = cost
                        best_col = col
                row = board.count_pieces(best_col)
                board.board[best_col][row] = board.turn
                if board.checkWin(board.turn):
                    label = FONT.render(board.label, 1, board.color)
                    game = False
                board.turn = PLAYER_PIECE
                board.set_label_color()

            board.draw(WINDOW)
            pygame.display.update()
            if label != None:
                WINDOW.blit(label, (40, 10))
                pygame.display.update()
            if game == False:
                pygame.time.wait(10000)
        pygame.quit()

    # elif type == 3 and method == 2:
    #     print('computer VS computer -> alphabeta')
    #     while game or moves != 0:
    #         clock.tick(FPS)
    #         if board.turn == PLAYER_PIECE and game != False:
    #             best_cost = +math.inf
    #             best_col = 0
    #             for(col, newboard) in board.successors(PLAYER_PIECE):
    #                 cost = alphabeta(newboard, 3,math.inf,-math.inf,True)
    #                 if  best_cost > cost:
    #                     best_cost = cost
    #                     best_col = col
    #             row = board.count_pieces(best_col)
    #             board.board[best_col][row] = board.turn
    #             if board.checkWin(board.turn):
    #                 label = FONT.render(board.label,1,board.color)
    #                 game = False
    #             board.turn = COMPUTER_PIECE
    #             board.set_label_color()

    #         pygame.time.wait(2500)

    #         if board.turn == COMPUTER_PIECE and game != False:
    #             best_cost = -math.inf
    #             best_col = 0
    #             for(col, newboard) in board.successors(COMPUTER_PIECE):
    #                 cost = alphabeta(newboard, 3,-math.inf,math.inf,False)
    #                 if cost > best_cost:
    #                     best_cost = cost
    #                     best_col = col
    #             row = board.count_pieces(best_col)
    #             board.board[best_col][row] = board.turn
    #             if board.checkWin(board.turn):
    #                 label = FONT.render(board.label,1,board.color)
    #                 game = False
    #             board.turn = PLAYER_PIECE
    #             board.set_label_color()

    #         moves -=2
    #         board.draw(WINDOW)
    #         pygame.display.update()
    #         if label != None:
    #             WINDOW.blit(label,(40, 10))
    #             pygame.display.update()
    #         if game == False:
    #             pygame.time.wait(10000)
    #     if moves == 0:
    #         WINDOW.blit(tie,(40, 10))
    #         pygame.display.update()
    #     pygame.quit()

    elif type == 2 and method == 3:
        print("player VS computer -> montecarlo")
        while game:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
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
                            game, label = humam_output(event, label, board, WINDOW, FONT)
                            board.draw(WINDOW)
                            pygame.display.update()
                            board.turn = COMPUTER_PIECE
                            board.set_label_color()

            if board.turn == COMPUTER_PIECE and game != False:
                best_col = monte_carlo(newboard)
                row = board.count_pieces(best_col)
                board.board[best_col][row] = board.turn
                if board.checkWin(board.turn):
                    label = FONT.render(board.label, 1, board.color)
                    game = False
                board.turn = PLAYER_PIECE
                board.set_label_color()

            board.draw(WINDOW)
            pygame.display.update()
            if label != None:
                WINDOW.blit(label,(40, 10))
                pygame.display.update()
            if game == False:
                pygame.time.wait(10000)
        pygame.quit()

main()
