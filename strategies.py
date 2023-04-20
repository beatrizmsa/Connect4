from board import *
from constant import *
from concurrent.futures import ThreadPoolExecutor
import math, os, random, time

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
    root = Node(board)
    start_time = time.time()
    while time.time() - start_time < limit:
        node = root
        while not node.is_leaf():
            node = node.select_child()
        if not node.is_fully_expanded():
            node.expand()
            node = random.choice(node.children)
        node.wins += rollout(node.game)
        node.visits += 1
    return max(root.children, key = lambda c: c.visits).game.last_move

def rollout(board):
    while not board.is_winner():
        board = random.choice(board.successors()[0])[1]
    return board.utility()

TIME = 0.5
C = math.sqrt(2)


class Node:
    def _init_(self, game, parent = None):
        self.game = game
        self.parent = parent
        self.children = []
        self.wins = 0
        self.visits = 0

    def is_leaf(self):
        return len(self.children) == 0

    def is_fully_expanded(self):
        possible_moves, _ = successors(self.game)
        return len(self.children) == len(possible_moves)

    def expand(self):
        possible_moves, _ =  game.successors()
        for move in possible_moves:
            self.children.append(Node(move, self))

    def select_child(self):
        total_visits = math.log(self.visits)
        best_score = -float("inf")
        best_child = None
        for child in self.children:
            if child.visits == 0:
                score = float('inf')
            else:
                exploration_term = math.sqrt(math.log(total_visits + 1) / child.visits)
                score = child.wins / child.visits + C * exploration_term
            if score > best_score:
                best_score = score
                best_child = child
        return best_child

    def backpropagate(self, result):
        self.visits += 1
        self.wins += result
        if self.parent is not None:
            self.parent.backpropagate(result)


def monte_carlo_tree_search(game, T = 1, num_threads = os.cpu_count()):
    def simulate(game):
        while game:
            possible_moves, _ = successors(game)
            game = random.choice(possible_moves)
        if game.get_winner() == "X":
            return 1
        else:
            return -1

    root = Node(game)
    ti = time()
    tf = time()
    execution_times = []
    nodes_expanded = []
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        while tf - ti < T:
            node = root

            # Select
            while not node.is_leaf():
                node = node.select_child()

            # Expand
            node.expand()
            new_node = random.choice(node.children)

            # Simulate
            futures = []
            possible_moves, _ = successors(new_node.game)
            for move in possible_moves:
                futures.append(executor.submit(simulate, move))

            results = [f.result() for f in futures]
            result = sum(results) / len(results)

            # Back propagate
            new_node.backpropagate(result)
            tf = time()

            # Keep track of execution time and nodes expanded
            execution_times.append(tf - ti)
            nodes_expanded.append(root.visits)

    # Choose best move
    best_score = float("-inf")
    best_move = None
    for child in root.children:
        score = child.wins / child.visits
        if score > best_score:
            best_score = score
            best_move = child.game.get_last_move()

    # Return results and metrics
    return best_move, execution_times, nodes_expanded





def monte_carlo(game):
    best_move, execution_times, nodes_expanded = monte_carlo_tree_search(game, TIME)
    return best_move
