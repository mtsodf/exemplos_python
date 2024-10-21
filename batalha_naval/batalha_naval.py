"""Crie um jogo de batalha naval onde o computador sorteia um local do barco e o usuário deve tentar acertar onde está o barco."""

import random
import os

colunas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
linhas = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

palpites = []

N = 10

# Sorteio do Barco no Grid
tamanho_do_barco = 5
barco_linha = random.randrange(N)
barco_coluna = random.randrange(N - tamanho_do_barco + 1)
barco = []
for i in range(tamanho_do_barco):
    barco_coluna_letra = colunas[barco_coluna + i]
    barco.append(f"{barco_coluna_letra}-{barco_linha}")
# Fim do sorteio do Barco no Grid
print(barco)

num_acertos = 0

while num_acertos < tamanho_do_barco:

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

    if palpite in barco:
        num_acertos += 1
