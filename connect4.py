from random import randint

ROW_COUNT = 7
COLUMN_COUNT = 6

def printBoard(matriz):
    top = '    1   2   3   4   5   6   7   '

    for j in range(0,COLUMN_COUNT):
        string = "   "
        j1 = 5 - j
        for i in range(0,ROW_COUNT):
            if(matriz[i][j1] != " "):
                string += " " + matriz[i][j1] + "  "
            else:
                string += ' -  '
        print(string)
    print(top)
    print(" ")

def countsplacedif(m, value):  # contar quantos espços estão ocupados em cada coluna
    count = 0
    for i in range(0, 6):
        if (m[value - 1][i] != ' '):
            count += 1
    return count

def checkWin(piece,matriz):   # verificar se há vitória
    for j in range(3,COLUMN_COUNT):     # horizontal
        for i in range(ROW_COUNT):
            if (matriz[i][j] == matriz[i][j - 1] == matriz[i][j - 2] == matriz[i][j - 3] == piece):
                    return True

    for j in range(COLUMN_COUNT): # vertical
        for i in range(3, ROW_COUNT):
            if (matriz[i][j] == matriz[i - 1][j] == matriz[i - 2][j] == matriz[i - 3][j] == piece):
                    return True

    # diagonal
    for i in range(0,4):
        for j in range(0, 3):
            if (matriz[j][i] == matriz[j + 1][i + 1] == matriz[j + 2][i + 2] == matriz[j + 3][i + 3] == piece or
                matriz[j + 3][i] == matriz[j + 2][i + 1] == matriz[j + 1][i + 2] == matriz[j][i + 3] == piece):
                    return True

    return False

def check_subset_pontuation(count_O, count_X): # verificar a pontuação de cada sub-conjunto
    pontuation = 0
    if count_O == 3 and count_X == 0:
        pontuation -= 50
    elif count_X == 3 and count_O == 0:
        pontuation += 50
    elif count_O == 2 and count_X == 0:
        pontuation -= 10
    elif count_X == 2 and count_O == 0:
        pontuation += 10
    elif count_O == 1 and count_X == 0:
        pontuation -= 1
    elif count_X == 1 and count_O == 0:
        pontuation += 1
    return pontuation

def utilidade(m): # m é a arvore
    pontuation = 0
    # verificar vertical
    for j in range(7):
        for i in range(3):
            count_O = 0
            count_X = 0
            for k in range(i, i + 4):
                if (m[j][k] == 'X'):
                    count_X += 1
                elif (m[j][k] == 'O'):
                    count_O += 1
            pontuation += check_subset_pontuation(count_O, count_X)

    # verificar horizontal
    for i in range(6):
        for j in range(4):
            count_O = 0
            count_X = 0
            for k in range(j, j + 4):
                if m[k][i] == 'X':
                    count_X += 1
                elif m[k][i] == 'O':
                    count_O += 1
            pontuation += check_subset_pontuation(count_O, count_X)

    # verificar diagonal
    for j in range(0,4):
        for i in range(0, 3):
            count_O = 0
            count_X = 0
            for k in range(0,4):
                if m[j + k][i + k] == 'X':
                    count_X +=1
                elif m[j + k][i + k] == 'O':
                    count_O += 1
            pontuation += check_subset_pontuation(count_O, count_X)

    for j in range(3,7):
        for i in range(0, 3):
            count_O = 0
            count_X = 0
            for k in range(0,4):
                if m[j - k][i + k] == 'X':
                    count_X +=1
                elif m[j - k][i + k] == 'O':
                    count_O += 1
            pontuation += check_subset_pontuation(count_O, count_X)

    return pontuation


def playerinput(piece, matriz):
    Set0 = { 1,2,3,4,5,6,7}
    pos = int(input('Your move: '))
    if (pos not in Set0):
        print('Input must be integer between 1 and 7')
        playerinput(piece, matriz)
    else:
        difspace = countsplacedif(matriz, pos)
        if difspace >= 6:
            print('Column full, try again.')
            playerinput(piece, matriz)

        else:
            matriz[pos-1][difspace] = piece
    return matriz

def Computermove(piece, matriz): # escolha random do computador
    pos = randint(1,7)
    difspace = countsplacedif(matriz, pos)
    if difspace >= 6:
        Computermove(piece, matriz)
    else:
        matriz[pos - 1][difspace] = piece

    return matriz


def main():
    while True:
        player = str( input('Choose X or O: ') )
        if player == 'X' or player == 'O':
            break

    playPiece = 'X'

    m = [[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],
         [" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]

    count = 0

    printBoard(m)

    while count < 42: # se chegar às 42 jogadas e ainda não tiver ocorrido uma vitória, declara-se empate
        count += 1

        if playPiece == player:
            m = playerinput(playPiece,m)
            print("Player")
            printBoard(m)
            print(utilidade(m))

        else:
            m = Computermove(playPiece,m)
            print("Computer")
            printBoard(m)
            print(utilidade(m))

        if checkWin(playPiece,m):
            print("Good Game: " + playPiece +  " win's")
            return

        if playPiece == 'X':
            playPiece = 'O'

        else:
            playPiece = 'X'

main()
