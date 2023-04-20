import pygame, copy, random
from constant import *

class Board:
    def __init__(self) -> None:
        self.board = [[" "," "," "," "," "," "],
                     [" "," "," "," "," "," "],
                     [" "," "," "," "," "," "],
                     [" "," "," "," "," "," "],
                     [" "," "," "," "," "," "],
                     [" "," "," "," "," "," "],
                     [" "," "," "," "," "," "]]
        self.selected_piece = None
        self.moves = 0
        self.turn = PLAYER_PIECE
        self.color = self.set_color()
        self.label = self.set_label()

    def set_color(self):
        if self.turn == PLAYER_PIECE:
            color = DEEPSKYBLUE
        else:
            color = STEELBLUE
        return color

    def set_label(self):
        if self.turn == PLAYER_PIECE:
            label = "light blue player wins !"
        else:
            label = "dark blue player wins !"
        return label

    def set_label_color(self):
        self.color = self.set_color()
        self.label = self.set_label()

    def set_turn(self):
        if self.turn == PLAYER_PIECE:
            turn = COMPUTER_PIECE
        else:
            turn = PLAYER_PIECE
        return turn

    def count_pieces(self, col):
        count = 0
        for i in range(0, 6):
            if (self.board[col][i] != ' '): #
                count += 1
        return count

    def checkWin(self, piece):
        # horizontal
        for j in range(3,ROWS):
            for i in range(COLS):
                if (self.board[i][j] == self.board[i][j - 1] == self.board[i][j - 2] == self.board[i][j - 3] == piece):
                        return True

        # vertical
        for j in range(ROWS):
            for i in range(3, COLS):
                if (self.board[i][j] == self.board[i - 1][j] == self.board[i - 2][j] == self.board[i - 3][j] == piece):
                        return True

        # diagonal
        for i in range(0, 3):
            for j in range(0, 4):
                if (self.board[j][i] == self.board[j + 1][i + 1] == self.board[j + 2][i + 2] == self.board[j + 3][i + 3] == piece or
                    self.board[j + 3][i] == self.board[j + 2][i + 1] == self.board[j + 1][i + 2] == self.board[j][i + 3] == piece):
                        return True
        return False

    def utility(self):
        pontuation = 0

        if self.checkWin(COMPUTER_PIECE):
            return 512

        if self.checkWin(PLAYER_PIECE):
            return -512

        else:
            # verificar vertical
            for j in range(COLS):
                for i in range(3):
                    count_O = 0
                    count_X = 0
                    for k in range(i, i + 4):
                        if (self.board[j][k] == PLAYER_PIECE):
                            count_O += 1
                        elif (self.board[j][k] == COMPUTER_PIECE):
                            count_X += 1
                    pontuation += check_subset_pontuation(count_O, count_X)

            # verificar horizontal
            for i in range(ROWS):
                for j in range(COLS - 3):
                    count_O = 0
                    count_X = 0
                    for k in range(j, j + 4):
                        if self.board[k][i] == PLAYER_PIECE:
                            count_O += 1
                        elif self.board[k][i] == COMPUTER_PIECE:
                            count_X += 1
                    pontuation += check_subset_pontuation(count_O, count_X)

            # verificar diagonal contraria
            for j in range(COLS - 3):
                for i in range(0, 3):
                    count_O = 0
                    count_X = 0
                    for k in range(0, 4):
                        if self.board[j + k][i + k] == PLAYER_PIECE:
                            count_O += 1
                        elif self.board[j + k][i + k] == COMPUTER_PIECE:
                            count_X += 1
                    pontuation += check_subset_pontuation(count_O, count_X)

            # verificar diagonal principal
            for j in range(3, COLS):
                for i in range(0, 3):
                    count_O = 0
                    count_X = 0
                    for k in range(0, 4):     # controla os incrementos dos i's e os decrementos dos j's
                        if self.board[j - k][i + k] == PLAYER_PIECE:
                            count_O += 1
                        elif self.board[j - k][i + k] == COMPUTER_PIECE:
                            count_X += 1
                    pontuation += check_subset_pontuation(count_O, count_X)

        return pontuation

    def draw(self,wind):
        wind.fill(SNOW)      # cria um fundo branco
        for c in range(COLS):
            for r in range(ROWS):
                pygame.draw.rect(wind, LIGHTSTEEL, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.circle(wind, SNOW, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), int(r*SQUARE_SIZE+SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)

        for c in range(COLS):
            for r in range(ROWS):
                if self.board[c][r] == PLAYER_PIECE:
                    pygame.draw.circle(wind, DEEPSKYBLUE, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), HEIGHT-int(r*SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
                elif self.board[c][r] == COMPUTER_PIECE:
                    pygame.draw.circle(wind, STEELBLUE, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), HEIGHT-int(r*SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)

    def is_winner(self):
        return self.checkWin(COMPUTER_PIECE) or self.checkWin(PLAYER_PIECE)

    def printBoard(self):
        top = '    1   2   3   4   5   6   7   '

        for j in range(0, ROWS):
            string = "   "
            j1 = 5 - j
            for i in range(0, COLS):
                if(self.board[i][j1] != " "):
                    string += " " + self.board[i][j1] + "  "
                else:
                    string += ' -  '
            print(string)
        print(top)
        print(" ")

    def successors(self,piece):     # board é o tabuleiro atual sem a jogada resultante do computador
        successors = []             # guardar todos os successores do nó atual
        for col in range(COLS):
            newboard = Board()
            newboard.board = copy.deepcopy(self.board)
            row = self.count_pieces(col)       # contar a quantidade de espaços ocupados em cada coluna do tabuleiro (i) e colocamos a peça na linha correspondente a esse valor
            if row != ROWS:                    # só se coloca um peça nessa coluna se a mesma não estiver totalmente ocupada
                newboard.board[col][row] = piece
                successors.append((col,newboard))
                if newboard.checkWin(piece):
                    list = []
                    list.append((col,newboard))
                    return list
        return successors

def check_subset_pontuation(count_O, count_X): # verificar a pontuação de cada sub-conjunto
        pontuation = 0
        if count_O == 3 and count_X == 0:
            pontuation -= 50
        if count_X == 3 and count_O == 0:
            pontuation += 50
        if count_O == 2 and count_X == 0:
            pontuation -= 10
        if count_X == 2 and count_O == 0:
            pontuation += 10
        if count_O == 1 and count_X == 0:
            pontuation -= 1
        if count_X == 1 and count_O == 0:
            pontuation += 1
        return pontuation

def simulate(self):
        if self.is_winner():
            return self.utility()
        else:
            col = random.randint(0, COLS - 1)
            while not self.is_valid(col):
                col = random.randint(0, COLS - 1)
            newboard = self.copy()
            newboard.add_piece(col, PLAYER_PIECE)
            return newboard.simulate()
