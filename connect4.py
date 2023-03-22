from random import randint

def printBoard(matriz):
    top = '    1   2   3   4   5   6   7   '
    
    for j in range(0,6):
        string = "   "   
        j1 = 5 -j
        for i in range(0,7):
            if(matriz[i][j1] != " "):
                string += " " + matriz[i][j1] +"  "
            else:
                string += ' -  '
        print(string) 
    print(top)
    print(" ")
    
def countsplacedif(m, valeu):  #contar quantos espços estão ocupados em cada coluna
    count = 0
    for i in range(0,7):
        if (m[valeu-1][i] != ' '):
            count += 1
    return count

def checkWin(piece,matriz):   #verificar se há vitória
    # Horizontal checker
    for j in range(0,6):
        for i in range(3,7):
            if (matriz[j][i]==matriz[j][i-1]==matriz[j][i-2]==matriz[j][i-3]==piece):
                    return True
            else:
                continue   
    # Vertical checker
    for i in range(0,7):
        for j in range(3,6):
            if (matriz[j][i]==matriz[j-1][i]==matriz[j-2][i]==matriz[j-3][i]==piece):
                    return True
            else:
                continue
    # Diagonal checker
    for i in range(0,4):
        for j in range(0,3):
            if (matriz[j][i]==matriz[j+1][i+1]==matriz[j+2][i+2]==matriz[j+3][i+3]==piece or
                matriz[j+3][i]==matriz[j+2][i+1]==matriz[j+1][i+2]==matriz[j][i+3]==piece):
                    return True
            else:
                continue
    return False

def playerinput(piece, matriz):
    Set0 = { 1,2,3,4,5,6,7}
    pos = int(input('Your move: '))
    if (pos not in Set0):
        print('Input must be integer between 1 and 7')
        playerinput(piece, matriz)
    else:
        difspace = countsplacedif(matriz, pos)
        if difspace >= 6:
            print('Column full, try again...')
            playerinput(piece, matriz)
            
        else:
            matriz[pos-1][difspace] = piece   
    return matriz

def Computermove(piece, matriz): #escolha random do computador
    pos = randint(1,7)
    difspace = countsplacedif(matriz, pos)
    if difspace >= 6:
        Computermove(piece, matriz)   
    else:
        matriz[pos-1][difspace] = piece

    return matriz


def main():

    while True:
        player = str( input('Choose X or O: ') )
        if player == 'X' or player == 'O':
            break
    
    playPiece = 'X'

    m = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]\
         ,[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
    
    count = 0

    printBoard(m)

    while count < 42: #se chegar às 42 jogadas e ainda não tiver ocorrido uma vitória, declara-se empate
        count += 1

        if playPiece == player:
            m = playerinput(playPiece,m)
            print("Player")
            printBoard(m)

        else:
            m= Computermove(playPiece,m)
            print("Computer")
            printBoard(m)
        
        if checkWin(playPiece,m):
            print("Good Game: " + playPiece +  " win's")
            return
 
        if playPiece == 'X':
            playPiece = 'O'

        else:
            playPiece = 'X'

main()



'''
import numpy as np

def create_board():
    board = np.zeros((6,7))
    print(board)

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[5][col] == 0

def get_next_open_row(board, col):
    for r in range(6):
        if board[r][col] == 0:
            return r

def print_board(board):
    board = np.flip(board, 0)
    print(board)

def winning_move(board, piece):
    return True

def play_game():
    board = create_board()
    print_board(board)
    game_over = False
    turn = 0

    while not game_over:
        # Ask for Player 1 input
        if turn == 0:
            col = int(input("Player 1 make your selection (1-7): ")) - 1

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1)

                if winning_move(board, 1):
                    print("Player 1 wins!")
                    game_over = True

        # Ask for Player 2 input
        else:
            col = int(input("Player 2 make your selection (1-7): ")) - 1

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)

                if winning_move(board, 2):
                    print("Player 2 wins!")
                    game_over = True

        print_board(board)

        turn += 1
        turn = turn % 2

play_game()
'''