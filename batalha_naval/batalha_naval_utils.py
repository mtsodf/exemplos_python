import random
import os

colunas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
linhas = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def imprimir_tabuleiro(palpites, barcos, mostrar_barcos=False):
    print(" ", " ".join(colunas))
    for linha in linhas:
        print(linha, end=" ")

        for coluna in colunas:

            posicao = f"{coluna}-{linha}"

            if mostrar_barcos:
                esta_em_um_barco = False
                if posicao_esta_em_um_barco(posicao, barcos):
                    print("b", end=" ")
                else:
                    print("x", end=" ")
            else:
                if posicao in palpites:
                    if posicao_esta_em_um_barco(posicao, barcos):
                        print("B", end=" ")
                    else:
                        print("o", end=" ")
                else:
                    print("x", end=" ")
        print()


def posicao_esta_em_um_barco(posicao, barcos):
    for barco in barcos:
        if posicao in barco:
            return True
    return False


def sortear_barcos(tamanho_do_barco=5):
    N = len(linhas)
    barco_linha = random.randrange(N)
    barco_coluna = random.randrange(N - tamanho_do_barco + 1)
    barco = []
    for i in range(tamanho_do_barco):
        barco_coluna_letra = colunas[barco_coluna + i]
        barco.append(f"{barco_coluna_letra}-{barco_linha}")

    return [barco]


def pegar_palpite_do_usuario(palpites):
    palpite_valido = False
    while not palpite_valido:
        palpite = input("Digite um palpite (Letra-Numero):")

        if len(palpite) != 3:
            print("Tamanho do palpite deve ser 3")
        elif palpite[0] not in colunas:
            print("O primeiro caractere deve ser uma letra de A a J")
        elif palpite[1] != "-":
            print("O segundo caractere deve ser o -")
        elif palpite[2] not in linhas:
            print("O terceiro caractere deve ser um número de 0 a 9")
        elif palpite in palpites:
            print("Não pode repetir palpite")
        else:
            palpite_valido = True
            palpites.append(palpite)
            os.system("clear")
    return palpite
