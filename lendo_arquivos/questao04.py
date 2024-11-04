"""
Questão 4: Filmes/Séries Lançados antes de 2010
	Enunciado: Liste os dez melhores filmes lançados até 2010.
"""

from questao01 import read_csv


cabecalho, dados = read_csv("./imdb_data.csv")

coluna_ano = cabecalho.index("releaseYear")
coluna_tipo = cabecalho.index("type")
coluna_titulo = cabecalho.index("title")
coluna_nota = cabecalho.index("averageRating")

filmes_selecionados = []

for dado in dados:
    ano = int(dado[coluna_ano])
    tipo = dado[coluna_tipo]
    titulo = dado[coluna_titulo]
    nota = float(dado[coluna_nota])

    if ano < 2010 and tipo == "movie":
        filmes_selecionados.append((nota, ano, titulo))


# Ordena a lista da menor nota pra maior nota
filmes_selecionados.sort()

# Inverte a lista filmes_selecionados
filmes_selecionados = filmes_selecionados[::-1]

for filme in filmes_selecionados[:10]:
    print(filme)
