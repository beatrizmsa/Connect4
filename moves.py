from board import draw_board
from numpy import np

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[0][col] == 0

def get_next_open_row(board, col):
    for r in range(len(board)):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

board = np.zeros((6,7), dtype=int)
game_over = False
turn = 0

while not game_over:
    # jogador 1
    if turn == 0:
        col = int(input("Jogador 1, faz a tua jogada (1-7): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)
            print_board(draw_board(board))
            turn += 1
    # jogador 2
    else:
        col = int(input("Jogador 2, faz a tua jogada (1-7): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
            print_board(draw_board(board))
            turn -= 1
