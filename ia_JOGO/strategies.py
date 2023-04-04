from board1 import *
    
def minimax(node, depth, maximizingPlayer):

    if depth == 0:         # definir uma função para verificar se o no atual é folha da árvore
        return node.utility(), None
    if maximizingPlayer:
        best_col = 0
        best_cost = float('-inf')
        for (col,newboard) in node.successors(COMPUTER_PIECE):
            cost, _ = minimax(newboard, depth - 1, False)
            if newboard.is_winner():
                best_cost = cost    
                best_col = col
                return best_cost, best_col
            if cost > best_cost:
                best_cost = cost
                best_col = col
        return best_cost, best_col
    else:
        best_col = 0
        best_cost = float('+inf')
        for (col,newboard) in node.successors(PLAYER_PIECE):
            cost, _ = minimax(newboard, depth - 1, True)
            if best_cost > cost:
                best_cost = cost
                best_col = col
        return best_cost, best_col