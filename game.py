from auxFunctions import count_pieces
import copy

COLUMN_COUNT = 7
ROW_COUNT = 6
PLAYER_PIECE = 'X'
COMPUTER_PIECE = 'O'

class board_game:
    def __init__(self, board, player_turn, utility = 0):
        self.board = board
        self.player_turn = player_turn
        self.utility = utility
