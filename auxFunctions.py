
from utility import utility
import copy

COLUMN_COUNT = 7
ROW_COUNT = 6
PLAYER_PIECE = 'X'
COMPUTER_PIECE = 'O'

def printBoard(board):
    top = '    1   2   3   4   5   6   7   '

    for j in range(0, ROW_COUNT):
        string = "   "
        j1 = 5 - j
        for i in range(0, COLUMN_COUNT):
            if(board[i][j1] != " "):
                string += " " + board[i][j1] + "  "
            else:
                string += ' -  '
        print(string)
    print(top)
    print(" ")


def count_pieces(board, value):               # contar quantos espaços estão ocupados em cada coluna
    count = 0

    for i in range(0, 6):
        if (board[value][i] != ' '): #
            count += 1
    return count                              # retorna a quantidade de peças que estão numa coluna


def player_input(board):
    Set0 = {1, 2, 3, 4, 5, 6, 7}
    position = int(input('Your move: '))

    if (position not in Set0):
        print('Input must be integer between 1 and 7')
        player_input(board)
    else:
        occupped_pieces = count_pieces(board, position - 1)
        if occupped_pieces >= 6:
            print('Column full, try again.')
            player_input(board)

        else:
            board[position - 1][occupped_pieces] = PLAYER_PIECE
    return board

'''
def computer_move(piece, board):              # escolha random do computador
    position = randint(1, 7)
    occupped_pieces = count_pieces(board, position - 1)

    if occupped_pieces >= 6:
        computer_move(piece, board)
    else:
        board[position - 1][occupped_pieces] = piece

    return board
'''
def computer_move(board):
    _,col = minimax(board, 3, True)
    occupped_pieces = count_pieces(board, col)
    board[col][occupped_pieces] = COMPUTER_PIECE
    return board


def successors(board,depth):     # board é o tabuleiro atual sem a jogada resultante do computador
        successors = []    # guardar todos os successores do nó atual
        for i in range(COLUMN_COUNT):
            newboard = copy.deepcopy(board)              # copiar o nó atual e gerar todos os seus successores
            occuped_pieces = count_pieces(board, i)      # contar a quantidade de espaços ocupados em cada coluna do tabuleiro (i) e colocamos a peça na linha correspondente a esse valor
            if occuped_pieces != ROW_COUNT:              # só se coloca um peça nessa coluna se a mesma não estiver totalmente ocupada
                if depth % 2 != 0:
                    newboard[i][occuped_pieces] = PLAYER_PIECE
                    successors.append(newboard)
                else:
                    newboard[i][occuped_pieces] = COMPUTER_PIECE
                    successors.append(newboard)
            else:
                successors.append(None)
        return successors

def minimax(node, depth, maximizingPlayer):
    best_col = 0
    i = 0

    if depth == 0:         # definir uma função para verificar se o no atual é folha da árvore
        return utility(node), None
    if maximizingPlayer:
        best_cost = float('-inf')
        for child in successors(node, depth):
            if child != None:
                cost, _ = minimax(child, depth - 1, False)
                if cost > best_cost:
                    best_cost = cost
                    best_col = i
            i += 1
        return best_cost, best_col
    else:
        best_cost = float('+inf')
        for child in successors(node, depth):
            if child != None:
                cost, _ = minimax(child, depth - 1, True)
                if cost < best_cost:
                    best_cost = cost
                    best_col = i
            i += 1
        return best_cost, best_col
