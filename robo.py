"""Um robô aspirador deve aspirar um cômodo retangular de comprimento 10m x 20m. Escreva um código mostrando para onde o robô deve se movimentar em cada metro quadrado. Print as setas com os seguintes caracteres:
print("Seta para cima:", '\u2191’) 
print("Seta para baixo:", '\u2193’) 
print("Seta para a esquerda:", '\u2190’) 
print("Seta para a direita:", '\u2192') """

seta_direita = '\u2192'
seta_baixo = '\u2193'
seta_esquerda = '\u2190'

nlinhas = 10
ncolunas = 20

for j in range(nlinhas):
    if j % 2 == 0:
        for i in range(ncolunas):
            if i == ncolunas - 1:
                print(seta_baixo, end=" ")
            else:
                print(seta_direita, end=" ")
    else:
        for i in range(ncolunas):
            if i == 0:
                print(seta_baixo, end=" ")
            else:
                print(seta_esquerda, end=" ")
    print("")
