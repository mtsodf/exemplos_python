"""
Crie uma função para contar quantas vezes cada palavra aparece em um texto. A função
deve receber uma string como entrada e retornar um dicionário onde as chaves são as
palavras e os valores são as contagens correspondentes
"""


def contar_palavras(texto):

    contagem = {}

    for palavra in texto.split():
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    return contagem


def contar_palavras_get(texto):
    contagem = {}

    for palavra in texto.split():
        contagem[palavra] = contagem.get(palavra, 0) + 1

    return contagem


arquivo = open("casmurro.txt", "r")
texto = arquivo.read()
arquivo.close()

texto = texto.lower()
texto = texto.replace("-", "")
texto = texto.replace(".", "")
texto = texto.replace(",", "")
texto = texto.replace("!", "")
texto = texto.replace("?", "")


contagem = contar_palavras_get(texto)

palavras = ["capitú", "bentinho", "escobar", "casmurro"]

for palavra in palavras:
    print(f"{palavra} => {contagem[palavra]}")
