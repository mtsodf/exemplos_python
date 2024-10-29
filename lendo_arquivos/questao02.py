"""
Questão 2: Filmes e Séries com Maior Avaliação
	Enunciado: Qual filme ou série tem a maior avaliação (averageRating)?
"""

from questao01 import read_csv


cabecalho, dados = read_csv("./imdb_data.csv")

coluna_titulo = cabecalho.index("title")
coluna_nota = cabecalho.index("averageRating")
coluna_votacao = cabecalho.index("numVotes")


print("*" * 40)
print("Solução 00".center(40))
print("*" * 40)

melhor_nota = -1
melhor_titulo = None
melhor_votacao = -1

for dado in dados:
    titulo = dado[coluna_titulo]
    nota = float(dado[coluna_nota])
    votos = int(dado[coluna_votacao])

    if nota > melhor_nota:
        melhor_nota = nota
        melhor_titulo = titulo
        melhor_votacao = votos
    elif nota == melhor_nota and votos > melhor_votacao:
        melhor_nota = nota
        melhor_titulo = titulo
        melhor_votacao = votos

print(f"O programa com maior nota é {melhor_titulo} com nota de {melhor_nota}. Com uma votação de {melhor_votacao}")


print("*" * 40)
print("Solução 01".center(40))
print("*" * 40)
lista_dos_programas = []


for dado in dados:
    titulo = dado[coluna_titulo]
    nota = float(dado[coluna_nota])
    votos = int(dado[coluna_votacao])

    lista_dos_programas.append((nota, votos, titulo))


lista_dos_programas.sort()
lista_dos_programas = lista_dos_programas[::-1]

header_titulo = "Título"
header_nota = "Nota"
header_votos = "Votos"

print("-" * 50)
print(f"{header_titulo:30s}{header_nota:>10s}{header_votos:>10s}")
print("-" * 50)

for programa in lista_dos_programas[:10]:
    nota, votos, titulo = programa
    print(f"{titulo:30s}{nota:10.2f}{votos:10d}")
