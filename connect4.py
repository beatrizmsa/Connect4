from auxFunctions import printBoard, player_input, computer_move
from checkWin import checkWin

PLAYER_PIECE = 'X'
COMPUTER_PIECE = 'O'


def main():
    board = [[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],
             [" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]

    count = 0                                   #contar a quantidade de jogadas
    piece_Played = PLAYER_PIECE                 # peça atual -> jogador começa (computador é sempre o jogador 2)
    printBoard(board)

    while count < 42:                           # se chegar às 42 jogadas e ainda não tiver ocorrido uma vitória, declara-se empate
        count += 1

        if piece_Played == PLAYER_PIECE:
            board = player_input(board)
            print("Player")
            printBoard(board)
        else:
            board = computer_move(board)
            print("Computer")
            printBoard(board)

        if checkWin(piece_Played, board):
            print("Good Game: " + piece_Played +  " win's")
            return

        if piece_Played == PLAYER_PIECE:
            piece_Played = COMPUTER_PIECE

        else:
            piece_Played = PLAYER_PIECE
main()
