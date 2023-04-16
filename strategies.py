from board import *
from constant import *
import math

def minimax(board, depth, maximizingPlayer):

    if depth == 0 or board.is_winner():
        return board.utility()
    if maximizingPlayer:
        best_cost = -math.inf
        for (col,newboard) in board.successors(COMPUTER_PIECE):
            best_cost = max(best_cost,minimax(newboard, depth - 1, False))
        return best_cost
    else:
        best_cost = +math.inf
        for (col,newboard) in board.successors(PLAYER_PIECE):
            best_cost = min(best_cost,minimax(newboard, depth - 1, True))
        return best_cost
