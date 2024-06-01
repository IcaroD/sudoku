import random

N = 9
global board
board = [[0 for i in range(9)] for j in range(9)]

def verificar(tabuleiro, x, y, num): #Verifica se atende todas as regras
    for i in range(9):
        if tabuleiro[x][i] == num or tabuleiro[i][y] == num:
            return False

    for i in range((x // 3) * 3, (x // 3) * 3 + 3):
        for j in range((y // 3) * 3, (y // 3) * 3 + 3):
            if tabuleiro[i][j] == num:
                return False

    return True


def solve():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if verificar(board, i, j, num):
                        board[i][j] = num
                        if solve():
                            return True
                        board[i][j] = 0
                return False
    return True

def nivel(qte): #Vai colocar a dificuldade
    global board
    board = [[0 for i in range(9)] for j in range(9)]
    solve()
    indices = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(indices)
    for k in range(qte):
        i, j = indices.pop()
        board[i][j] = ""
    return board
