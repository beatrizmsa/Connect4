from board import *
from constant import *
from concurrent.futures import ThreadPoolExecutor
import math, os, random
from time import time

def minimax(board, depth, maximizingPlayer):

    if depth == 0 or board.is_winner():
        return board.utility(), None, board.visit
    
    if maximizingPlayer:
        best_cost = -math.inf
        best_col = []
        for (col, newboard) in board.successors(COMPUTER_PIECE):
            value,_, visit = minimax(newboard, depth - 1, False)
            if depth == MAX_DEPTH:
                if best_cost == value:
                    best_col.append(col)
                if value > best_cost:
                    best_cost = value
                    best_col = []
                    best_col.append(col)
            else:
                best_cost = max(best_cost, value)
            board.visit += visit
        return best_cost, best_col, board.visit
    
    else:
        best_cost = +math.inf
        best_col = []
        for (col, newboard) in board.successors(PLAYER_PIECE):
            value,_, visit = minimax(newboard, depth - 1, True)
            if depth == MAX_DEPTH:
                if best_cost == value:
                    best_col.append(col)
                if best_cost > value:
                    best_cost = value
                    best_col = []
                    best_col.append(col)
            else:
                best_cost = min(best_cost, value)
            board.visit += visit
        return best_cost, best_col, board.visit


def alphabeta(board, depth, alpha, beta, maximizingPlayer):

    if depth == 0 or board.is_winner():
        return board.utility(),None,board.visit
    
    if maximizingPlayer:
        best_cost = -math.inf
        best_col = []
        for (col, newboard) in board.successors(COMPUTER_PIECE):
            value,_,visit = alphabeta(newboard, depth - 1, alpha, beta, False)
            if depth == MAX_DEPTH:
                if best_cost == value:
                    best_col.append(col)
                if value > best_cost:
                    best_cost = value
                    best_col = []
                    best_col.append(col)
            else:
                best_cost = max(best_cost,value)
            board.visit += visit
            alpha = max(alpha, best_cost)
            if beta <= alpha:
                break
        return best_cost, best_col, board.visit
    
    else:
        best_cost = +math.inf
        best_col = []
        for (col, newboard) in board.successors(PLAYER_PIECE):
            value,_,visit = alphabeta(newboard, depth - 1, alpha, beta, True)
            if depth == MAX_DEPTH:
                if best_cost == value:
                    best_col.append(col)
                if best_cost > value:
                    best_cost = value
                    best_col = []
                    best_col.append(col)
            else:
                best_cost = min(best_cost,value)
            board.visit += visit
            beta = min(beta, best_cost)
            if beta <= alpha:
                break
        return best_cost, best_col, board.visit

class Node:
    def __init__(self,board,parent = None):
        self.board = board
        self.parent = parent
        self.children = []
        self.wins = 0
        self.visits = 0
        self.column_used = None
    
    def expand_node(self, turn):
        successors = self.board.successors(turn)
        if successors:
            for col, move in successors:
                move.set_turn()
                child = Node(move, self)
                child.column_used = col
                self.children.append(child)
    
    def update(self,result):
        self.visits += 1
        self.wins += result
    
    def is_leaf(self):
        return len(self.children) == 0
    
    def has_parent(self):
        return self.parent is not None
    
    def select_child(self):
        best_child = None
        best_value = - math.inf
        for child in self.children:
            if child.visits == 0 or self.visits <= 0:
                score = float('inf')
            else:
                exploit = child.wins / child.visits
                explore = C * math.sqrt(math.log(self.visits) / child.visits)
                score = exploit + explore
            if score > best_value:
                best_value = score
                best_child = child
        return best_child

    def simulation(self):
        possivel_moves = self.board.successors(self.board.turn)
        if len(possivel_moves) == 0:
            return self.board
        return random.choice(possivel_moves)[1]
    
def evaluate(board):
    if board.checkWin(COMPUTER_PIECE):
        return -1
    elif board.checkWin(PLAYER_PIECE):
        return  1
    else:
        return 0


def monte_carlos_tree_search(board, T):
    root = Node(board)
    ti = time()
    tf = time()
    while tf- ti < 0.00001:
        node = root
        s = copy.deepcopy(board)
        while not node.is_leaf():
            node = node.select_child()

        node.expand_node(node.board.turn)
        node = node.select_child()
        while node is not None:
            s = node.simulation()
        result = evaluate(s)
        
        while node.has_parent():
            node.update(result)
            node = node.parent
    
    best_score = float('-inf')
    best_move = 0
    for child in root.children:
        score = child.wins / child.visits
        if score >= best_score:
            best_score = score
            best_move = child.column_used
    return best_move
