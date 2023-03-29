COLUMN_COUNT = 7
ROW_COUNT = 6
PLAYER_PIECE = 'X'
COMPUTER_PIECE = 'O'

def check_subset_pontuation(count_O, count_X): # verificar a pontuação de cada sub-conjunto
    pontuation = 0
    if count_O == 3 and count_X == 0:
        pontuation -= 50
    elif count_X == 3 and count_O == 0:
        pontuation += 50
    elif count_O == 2 and count_X == 0:
        pontuation -= 10
    elif count_X == 2 and count_O == 0:
        pontuation += 10
    elif count_O == 1 and count_X == 0:
        pontuation -= 1
    elif count_X == 1 and count_O == 0:
        pontuation += 1
    return pontuation


def utility(board):
    pontuation = 0

    # verificar vertical
    for j in range(COLUMN_COUNT):
        for i in range(3):
            count_O = 0
            count_X = 0
            for k in range(i, i + 4):
                if (board[j][k] == PLAYER_PIECE):
                    count_X += 1
                elif (board[j][k] == COMPUTER_PIECE):
                    count_O += 1
            pontuation += check_subset_pontuation(count_O, count_X)

    # verificar horizontal
    for i in range(ROW_COUNT):
        for j in range(COLUMN_COUNT - 3):
            count_O = 0
            count_X = 0
            for k in range(j, j + 4):
                if board[k][i] == PLAYER_PIECE:
                    count_X += 1
                elif board[k][i] == COMPUTER_PIECE:
                    count_O += 1
            pontuation += check_subset_pontuation(count_O, count_X)

    # verificar diagonal contraria
    for j in range(COLUMN_COUNT - 3):
        for i in range(0, 3):
            count_O = 0
            count_X = 0
            for k in range(0, 4):
                if board[j + k][i + k] == PLAYER_PIECE:
                    count_X += 1
                elif board[j + k][i + k] == COMPUTER_PIECE:
                    count_O += 1
            pontuation += check_subset_pontuation(count_O, count_X)

    # verificar diagonal principal
    for j in range(3, COLUMN_COUNT):
        for i in range(0, 3):
            count_O = 0
            count_X = 0
            for k in range(0, 4):     # controla os incrementos dos i's e os decrementos dos j's
                if board[j - k][i + k] == PLAYER_PIECE:
                    count_X +=1
                elif board[j - k][i + k] == COMPUTER_PIECE:
                    count_O += 1
            pontuation += check_subset_pontuation(count_O, count_X)

    return pontuation
