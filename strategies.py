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
            value, _, visit = minimax(newboard, depth - 1, False)
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
            value, _, visit = minimax(newboard, depth - 1, True)
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
            value, _, visit = alphabeta(newboard, depth - 1, alpha, beta, False)
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
            value, _, visit = alphabeta(newboard, depth - 1, alpha, beta, True)
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
    def __init__(self, board, parent = None):
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
                move.moves += 1
                child = Node(move, self)
                child.column_used = col
                self.children.append(child)

    def update(self,result):
        self.visits += 1
        self.wins += result

    def is_leaf(self):
        if self.board.moves == 42 or self.board.is_winner():
            return True
        else:
            return len(self.children) == 0

    def has_parent(self):
        return self.parent is not None
    
    def is_fully_expanded(self):
        possible_moves = self.board.successors(self.board.turn)
        return len(self.children) == len(possible_moves)

    def select_child(self):
        best_value = -math.inf
        best_children = []
        unvisited_children = []
        for child in self.children:
            if child.visits == 0 or self.visits <= 0:
                unvisited_children.append(child)
            else:
                exploit = child.wins / child.visits
                explore = C * math.sqrt((2 * math.log(self.visits + 1) ) / child.visits)
                score = exploit + explore
                if score == best_value:
                    best_children.append(child)
                if score > best_value:
                    best_value = score
                    best_children = [child]
            if len (unvisited_children) > 0:
                return random.choice(unvisited_children)
        return random.choice(best_children)
    
def simulation(node):
    if node.moves != 42 or  not node.is_winner():
        possivel_moves = node.successors(node.turn)
        return evaluate(random.choice(possivel_moves)[1])

def evaluate(board):
    if board.checkWin(COMPUTER_PIECE):
        return 1
    else:
        return -1


def monte_carlos_tree_search(board, T, num_threads = os.cpu_count()):
    root = Node(board)
    ti = time()
    tf = time()
    with ThreadPoolExecutor(max_workers = num_threads) as executor:
        while tf - ti < T:
            node = root

            while not node.is_leaf():
                node = node.select_child()

            if not node.is_fully_expanded():
                node.expand_node(node.board.turn)
                new_node = random.choice(node.children)
            else:
                new_node = node.select_child()
             
            futures = []
            possible_moves = new_node.board.successors(new_node.board.turn)
            for (col, move) in possible_moves:
                futures.append(executor.submit(simulation, move))

            results = [f.result() for f in futures if f.result() is not None]
            if results:
                result = sum(results) / len(results)
            else:
                result = 0

            while node.has_parent():
                node.update(result)
                node = node.parent

            tf = time()

    best_score = float('-inf')
    best_move = 0
    for child in root.children:
        if child.visits == 0:
            score = 0
        else:
            score = child.wins / child.visits
        print(score)
        if score > best_score:
            best_score = score
            best_move = child.column_used
    return best_move
