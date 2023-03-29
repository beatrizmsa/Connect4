COLUMN_COUNT = 7
ROW_COUNT = 6

def checkWin(piece,matriz):      # verificar se há vitória
    # horizontal
    for j in range(3,ROW_COUNT):
        for i in range(COLUMN_COUNT):
            if (matriz[i][j] == matriz[i][j - 1] == matriz[i][j - 2] == matriz[i][j - 3] == piece):
                    return True

    # vertical
    for j in range(ROW_COUNT):
        for i in range(3, COLUMN_COUNT):
            if (matriz[i][j] == matriz[i - 1][j] == matriz[i - 2][j] == matriz[i - 3][j] == piece):
                    return True

    # diagonal
    for i in range(0, 3):
        for j in range(0, 4):
            if (matriz[j][i] == matriz[j + 1][i + 1] == matriz[j + 2][i + 2] == matriz[j + 3][i + 3] == piece or
                matriz[j + 3][i] == matriz[j + 2][i + 1] == matriz[j + 1][i + 2] == matriz[j][i + 3] == piece):
                    return True

    return False
