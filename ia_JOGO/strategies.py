from board1 import *
from constanc import *
import math
    
def minimax(node, depth, maximizingPlayer):

    if depth == 0 or node.is_winner():        # definir uma função para verificar se o no atual é folha da árvore
        return node.utility()
    if maximizingPlayer:
        best_cost = -math.inf
        for (col,newboard) in node.successors(COMPUTER_PIECE):
            best_cost = max(best_cost,minimax(newboard, depth - 1, False))
        return best_cost
    else:
        best_cost = +math.inf
        for (col,newboard) in node.successors(PLAYER_PIECE):
            best_cost = min(best_cost,minimax(newboard, depth - 1, True))
        return best_cost
    