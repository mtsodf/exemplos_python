"""
Questão 6: Top 3 Filmes ou Séries Mais Votados
	Enunciado: Liste os 3 filmes ou séries com o maior número de votos (numVotes).
"""

from questao01 import read_csv


# Versao da funcao sem list comprehension
def filtrar_midia_sem_lc(cabecalho, dados, tipo_de_midia="movie"):
    col_tipo = cabecalho.index("type")
    lista_filtrada = []
    for dado in dados:
        if dado[col_tipo] == tipo_de_midia:
            lista_filtrada.append(dado)
    return lista_filtrada


def filtrar_midia(cabecalho, dados, tipo_de_midia="movie"):
    col_tipo = cabecalho.index("type")
    return [dado for dado in dados if dado[col_tipo] == tipo_de_midia]


cabecalho, dados = read_csv("imdb_data.csv")

dados_filmes = filtrar_midia(cabecalho, dados, "movie")

lista_votos_filme = []
col_titulo = cabecalho.index("title")
col_votos = cabecalho.index("numVotes")

for dado in dados_filmes[:10]:
    titulo = dado[col_titulo]
    votos = int(dado[col_votos])
    lista_votos_filme.append((votos, titulo))

lista_votos_filme.sort(reverse=True)

for voto, filme in lista_votos_filme[:3]:
    print(f"{voto:10d}{filme:>20s}")
