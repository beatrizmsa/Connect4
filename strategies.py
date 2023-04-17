from board import *
from constant import *
import math

def minimax(board, depth, maximizingPlayer):

    if depth == 0 or board.is_winner():
        return board.utility()
    if maximizingPlayer:
        best_cost = -math.inf
        for (col, newboard) in board.successors(COMPUTER_PIECE):
            best_cost = max(best_cost,minimax(newboard, depth - 1, False))
        return best_cost
    else:
        best_cost = +math.inf
        for (col,newboard) in board.successors(PLAYER_PIECE):
            best_cost = min(best_cost,minimax(newboard, depth - 1, True))
        return best_cost

def alphabeta(board, depth, alpha, beta, maximizingPlayer):

    if depth == 0 or board.is_winner():
        return board.utility()
    if maximizingPlayer:
        best_cost = -math.inf
        for (col, newboard) in board.successors(COMPUTER_PIECE):
            best_cost = max(best_cost,alphabeta(newboard, depth - 1, alpha, beta, False))
            alpha = max(alpha, best_cost)
            if beta <= alpha:
                break
        return best_cost
    else:
        best_cost = +math.inf
        for (col, newboard) in board.successors(PLAYER_PIECE):
            best_cost = min(best_cost,alphabeta(newboard, depth - 1, alpha, beta, True))
            beta = min(beta, best_cost)
            if beta <= alpha:
                break
        return best_cost

def montecarlo(board, limit):

        if board.is_winner():
            return board.utility()
        best_cost = -math.inf
        for (col, newboard) in board.successors(COMPUTER_PIECE):
            cost = 0
            for i in range(limit):
                cost += newboard.simulate()
            cost = cost / limit
            if cost > best_cost:
                best_cost = cost
                best_col = col
        return best_col
