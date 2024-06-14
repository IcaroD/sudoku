from tkinter import *
from regras import Regras

# popup
def open_popup():
    top= Toplevel(root)
    top.geometry("400x250")
    top.title("Vitória")
    Label(top, text= "Você ganhou!", font=('Arial 20')).place(x=100,y=90)

celulas = {}
regra = Regras()


def facil():  # facil com 70 elementos
    errLabel.configure(text="")
    num = 10
    dificuldade(num)


def medio():  # medio com 60 elementos
    errLabel.configure(text="")
    num = 20
    dificuldade(num)


def dificil():  # facil com 40 elementos
    errLabel.configure(text="")
    num = 50
    dificuldade(num)


def dificuldade(total):  # põe a dificuldade
    board = regra.nivel(total)
    for linha in range(2, 11):
        for col in range(1, 10):
            celulas[(linha, col)].delete(0, "end")
            celulas[(linha, col)].insert(0, board[linha - 2][col - 1])


def num_digitado(P):  # Vê se, o que foi digitado é um número
    ilegal = (P.isdigit() or P == "") and len(P) < 2
    return ilegal


def draw3x3Grid(row, column, bgcolor):  # faz uma tabela de 3x3
    for i in range(3):
        for j in range(3):
            e = Entry(
                root,
                width=5,
                bg=bgcolor,
                justify="center",
                validate="key",
                validatecommand=(reg, "%P"),
            )
            e.grid(
                row=row + i + 1,
                column=column + j + 1,
                sticky="nsew",
                padx=1,
                pady=1,
                ipady=5,
            )
            celulas[(row + i + 1, column + j + 1)] = e


def draw9x9Grid():  # Junta as tabelas de 3x3
    color = "#FFFFFF"
    for tabelas_linha in range(1, 10, 3):
        for tabela_coluna in range(0, 9, 3):
            draw3x3Grid(tabelas_linha, tabela_coluna, color)
            if color == "#FFFFFF":
                color = "#D0ffff"
            else:
                color = "#FFFFFF"


def reset():  # renicia a tabela
    errLabel.configure(text="")
    for linha in range(2, 11):
        for col in range(1, 10):
            celula = celulas[(linha, col)]
            celula.delete(0, "end")


def getValues():  # Pega os valores e transforma em inteiros
    board = []
    for linha in range(2, 11):
        linhas = []
        for col in range(1, 10):
            val = celulas[(linha, col)].get()
            if val == "":
                linhas.append(0)
            else:
                linhas.append(int(val))
        board.append(linhas)
    return board

def valida_preenchimento(tabela):
    for linha in range(9):
        for coluna in range(9):
            if tabela[linha][coluna] == 0:  # valida preenchimento
                errLabel.configure(text=f"Preencha a celula {(linha+1,coluna+1)}, continue!")
                return False
    return True

def valida_linha(tabela):
    for i in range(9):
        for j in range(9):
            num = tabela[j][i]
            for k in range(9):
                if tabela[j][k] == num and k != i:
                    errLabel.configure(text=f"Error na linha {j+1}")
                    return False
    return True

def valida_coluna(tabela):
    for i in range(9):
        for j in range(9):
            num = tabela[i][j]
            for k in range(1, 9):
                if tabela[k][j] == num and k != i:
                    errLabel.configure(text=f"Error na coluna {j+1}")
                    return False
    return True
            
def valida_3x3(tabela):
    for x in range(9):
        for y in range(9):
            num = tabela[x][y]
            for i in range((x // 3) * 3, (x // 3) * 3 + 3):
                for j in range((y // 3) * 3, (y // 3) * 3 + 3):
                    if i != x and j != y:
                        if tabela[i][j] == num:
                            errLabel.configure(text=f"{num} aparece pelo menos 2 vezes, na célula {x+1,y+1} e {i+1,j+1}")
                            return False
    return True

def valida_jogo():  # Verifica, se venceu
    errLabel.configure(text="")
    tabela = getValues()
    ok = False
    if valida_preenchimento(tabela): 
        ok = True
    else:
        ok = False
        return None
    if valida_linha(tabela): 
        ok = True
    else:
        ok = False
        return None
    if valida_coluna(tabela): 
        ok = True
    else:
        ok = False
        return None
    if valida_3x3(tabela):
        ok = True
    else:
        ok = False
        return None
    if ok:
        open_popup()


root = Tk()
root.title("Sudoku")
root.geometry("324x550")

errLabel = Label(root, text="", fg="red")
errLabel.grid(row=15, column=1, columnspan=10, pady=5)

reg = root.register(num_digitado)  # registra o numero

btn_solved = Button(root, command=valida_jogo, text="Resolvido?", width=10)
btn_solved.grid(row=20, column=1, columnspan=5, pady=20)

btn_reset = Button(root, command=reset, text="Reset", width=10)
btn_reset.grid(row=20, column=5, columnspan=5, pady=20)

facil = Button(root, command=facil, text="Fácil", width=10)
facil.grid(row=21, column=3, columnspan=5, pady=1)

medio = Button(root, command=medio, text="Médio", width=10)
medio.grid(row=22, column=3, columnspan=5, pady=1)

dificil = Button(root, command=dificil, text="Difícil", width=10)
dificil.grid(row=23, column=3, columnspan=5, pady=1)

exit_button = Button(root, text="Exit", command=root.destroy, width=10)
exit_button.grid(row=25, column=3, columnspan=5, pady=7)

draw9x9Grid()
root.mainloop()
