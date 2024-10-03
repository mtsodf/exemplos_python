"""
Jogo adivinhação de palavras
"""

import string
import os
import random

letras = str(string.ascii_lowercase)
palavra = random.choice(["infnet", "mateus", "instituto", "outubro", "python"])
palpites = []

acertos = 0
erros = 0
while acertos < len(palavra) and erros < 5:
    os.system("clear")
    # Escreve o título do programa
    num_col = 50
    print("*" * num_col)
    print(" Jogo da Adivinhacao ".center(num_col, "*"))
    print("*" * num_col)

    # Escreve a palavra com as letras palpites a mostra
    linha = ""
    for letra in palavra:
        if letra in palpites:
            linha += letra + " "
        else:
            linha += "_ "

    print(linha.strip().center(num_col))

    print("")
    print(f"Acertos: {acertos}")
    print(f"Erros: {erros}")
    print("")

    palpite = None
    palpite_valido = False
    while not palpite_valido:
        palpite = input("Digite um palpite de letra: ")
        if palpite not in letras or palpite in palpites:
            palpite_valido = False
        else:
            palpite_valido = True
            palpites.append(palpite)
            count = palavra.count(palpite)
            if count > 0:
                acertos += count
            else:
                erros += 1

os.system("clear")
# Escreve o título do programa
num_col = 50
print("*" * num_col)
print(" Jogo da Adivinhacao ".center(num_col, "*"))
print("*" * num_col)

# Escreve a palavra com as letras palpites a mostra
linha = ""
for letra in palavra:
    if letra in palpites:
        linha += letra + " "
    else:
        linha += "_ "

print(linha.strip().center(num_col))

print("")
print(f"Acertos: {acertos}")
print(f"Erros: {erros}")
print("")

if acertos == len(palavra):
    print("Parabéns!! Você ganhou o jogo!")
else:
    print("Que pena! Você errou!")
