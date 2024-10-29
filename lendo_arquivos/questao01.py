"""
Questão 1: Carregar e Exibir o Conteúdo do CSV
Enunciado: Carregue o arquivo CSV e exiba as 5 primeiras linhas (sem contar o cabeçalho).
"""


def read_csv(caminho):
    arquivo = open(caminho, "r")
    linhas = arquivo.readlines()
    arquivo.close()

    dados_separados = []
    for linha in linhas:
        valores_separados = linha.strip().split(";")
        dados_separados.append(valores_separados)

    header = dados_separados[0]
    return header, dados_separados[1:]


header, dados_separados = read_csv("imdb_data.csv")

coluna_titulo = header.index("title")
coluna_rating = header.index("averageRating")

header_titulo = "Título"
header_nota = "Nota"

print("-" * 35)
print(f"{header_titulo:30s}{header_nota:5s}")
print("-" * 35)

for dados_linha in dados_separados[:5]:
    titulo = dados_linha[coluna_titulo]
    nota = dados_linha[coluna_rating]
    print(f"{titulo:30s}{nota:5s}")
