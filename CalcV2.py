import customtkinter as ctk

#variaveis resenhudas
n1 = None          # primeiro número
n2 = None          # segundo número
operacao = None    # +, -, * ou /
digitando = ""     # número que está sendo digitado agora (como texto)


def mostrar(texto):
    visor.configure(text=texto)

def formatar(numero):
    if numero == int(numero):
        return str(int(numero))
    return str(numero)


def clique_numero(numero):
    global digitando
    if numero == "." and "." in digitando:
        return  # não deixa colocar dois pontos
    digitando = digitando + numero
    mostrar(digitando)


# Quando clica em + - *  /
def clique_operacao(op):
    global n1, operacao, digitando
    if digitando == "":
        return  # precisa ter digitado um número antes
    n1 = float(digitando)  # primeironumero
    operacao = op
    digitando = ""
    mostrar(formatar(n1) + " " + op)


# Quando clica em =
def clique_igual():
    global n1, n2, operacao, digitando
    if n1 is None or digitando == "":
        return
    n2 = float(digitando)  # segundonumero

    if operacao == "+":
        resultado = n1 + n2
    elif operacao == "-":
        resultado = n1 - n2
    elif operacao == "*":
        resultado = n1 * n2
    elif operacao == "/":
        if n2 == 0:
            clique_limpar()
            mostrar("Erro")
            return
        resultado = n1 / n2

    print("n1 =", n1, "| n2 =", n2, "| resultado =", resultado)
    mostrar(formatar(resultado))

    digitando = formatar(resultado)
    n1 = None
    n2 = None
    operacao = None


# Quando o caba clica em C
def clique_limpar():
    global n1, n2, operacao, digitando
    n1 = None
    n2 = None
    operacao = None
    digitando = ""
    mostrar("0")


# Cores bruh
COR_FUNDO = "#152552"
COR_NUMERO = "#e0b068"
COR_NUMERO_HOVER = "#FAEDA3"
COR_OPERACAO = "#e0b068"
COR_OPERACAO_HOVER = "#ffb340"
COR_LIMPAR = "#558cb1"
COR_LIMPAR_HOVER = "#c4c4c4"

# GUImaldita
ctk.set_appearance_mode("dark")
janela = ctk.CTk()
janela.title("CalculadoraTESTE")
janela.geometry("550x620")
janela.configure(fg_color=COR_FUNDO)

visor = ctk.CTkLabel(
    janela,
    text="0",
    anchor="e",
    text_color="white",
    font=("Segoe UI", 56),
)
visor.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=20)

botoes = [
    ["C", "",  "",  "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "",  "="],
]

for linha, textos in enumerate(botoes, start=1):
    for coluna, texto in enumerate(textos):
        if texto == "":
            continue

        cor_texto = "white"
        if texto.isdigit() or texto == ".":
            acao = lambda t=texto: clique_numero(t)
            cor, cor_hover = COR_NUMERO, COR_NUMERO_HOVER
        elif texto == "=":
            acao = clique_igual
            cor, cor_hover = COR_OPERACAO, COR_OPERACAO_HOVER
        elif texto == "C":
            acao = clique_limpar
            cor, cor_hover = COR_LIMPAR, COR_LIMPAR_HOVER
            cor_texto = "black"
        else:
            acao = lambda t=texto: clique_operacao(t)
            cor, cor_hover = COR_OPERACAO, COR_OPERACAO_HOVER

        botao = ctk.CTkButton(
            janela,
            text=texto,
            command=acao,
            font=("Segoe UI", 28),
            fg_color=cor,
            hover_color=cor_hover,
            text_color=cor_texto,
            corner_radius=24,   # cantos bem redonduchos
            width=80,
            height=80,
        )
        botao.grid(row=linha, column=coluna, sticky="nsew", padx=6, pady=6)

# botoes grandes
for i in range(4):
    janela.columnconfigure(i, weight=1)
for i in range(6):
    janela.rowconfigure(i, weight=1)

# Manter a janela aberta
janela.mainloop()

