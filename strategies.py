from utility import utility
from auxFunctions import count_pieces
import copy

COLUMN_COUNT = 7
ROW_COUNT = 6
PLAYER_PIECE = 'X'
COMPUTER_PIECE = 'O'

def minimax(node, depth, maximizingPlayer):
    best_col = 0
    i = 0
    if depth == 0:         # definir uma função para verificar se o no atual é folha da árvore
        return utility(node), None
    if maximizingPlayer:
        best_utility = float('-inf')
        for child in successors(node):
            if child != None:
                utility = minimax(child, depth - 1, False)
                if utility > best_utility:
                    best_utility = utility
                    best_col = i
            i += 1
        return best_utility, best_col
    else:
        best_utility = float('+inf')
        for child in successors(node):
            if child != None:
                utility = minimax(child, depth - 1, True)
                if utility < best_utility:
                    best_utility = utility
                    best_col = i
            i += 1
        return best_utility, best_col

def successors(board):     # board é o tabuleiro atual sem a jogada resultante do computador
        successors = []    # guardar todos os successores do nó atual
        for i in range(COLUMN_COUNT):
            newboard = copy.deepcopy(board)              # copiar o nó atual e gerar todos os seus successores
            occuped_pieces = count_pieces(board, i)      # contar a quantidade de espaços ocupados em cada coluna do tabuleiro (i) e colocamos a peça na linha correspondente a esse valor
            if occuped_pieces != ROW_COUNT:              # só se coloca um peça nessa coluna se a mesma não estiver totalmente ocupada
                newboard[i][occuped_pieces] = COMPUTER_PIECE
                successors.append(newboard)
            else:
                successors.append(None)
        return successors

'''
def alphabeta(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0:         # definir uma função para verificar se o no atual é folha da árvore
        return utility(node)
    if maximizingPlayer:
        utility = float('-inf')
        for child in successors(node):
            utility = max(utility, minimax(child, depth -1, False))
            if utility > beta:
                break
            alpha = max(alpha, utility)
        return utility
    else:
        utility = float('+inf')
        for child in successors(node):
            utility = min(utility, minimax(child, depth -1, True))
            if utility < alpha:
                break
            beta = min(beta, utility)
        return utility
'''
