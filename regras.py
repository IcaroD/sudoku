import random


class Regras:
    def __init__(self) -> None:
        self.board = [[0 for i in range(9)] for j in range(9)]

    def verificar(self, tabuleiro, x, y, num):  # Verifica se atende todas as regras
        for i in range(9):
            if tabuleiro[x][i] == num or tabuleiro[i][y] == num:
                return False

        for i in range((x // 3) * 3, (x // 3) * 3 + 3):
            for j in range((y // 3) * 3, (y // 3) * 3 + 3):
                if tabuleiro[i][j] == num:
                    return False

        return True

    def solve(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    for num in range(1, 10):
                        if self.verificar(self.board, i, j, num):
                            self.board[i][j] = num
                            if self.solve():
                                return True
                            self.board[i][j] = 0
                    return False
        return True

    def nivel(self, qte):  # Vai colocar a dificuldade
        self.board = [[0 for i in range(9)] for j in range(9)]
        self.solve()
        indices = [(i, j) for i in range(9) for j in range(9)]
        random.shuffle(indices)
        for k in range(qte):
            i, j = indices.pop()
            self.board[i][j] = ""
        return self.board
