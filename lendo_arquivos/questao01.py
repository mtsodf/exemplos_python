"""
Questão 1: Carregar e Exibir o Conteúdo do CSV
Enunciado: Carregue o arquivo CSV e exiba as 5 primeiras linhas (sem contar o cabeçalho).
"""

arquivo = open("imdb_data.csv", "r")
linhas = arquivo.readlines()
arquivo.close()


coluna_titulo = 2
coluna_rating = 5

header_titulo = "Título"
header_nota = "Nota"

print("-" * 35)
print(f"{header_titulo:30s}{header_nota:5s}")
print("-" * 35)

for linha in linhas[1:6:1]:
    valores_separados = linha.strip().split(";")
    titulo = valores_separados[coluna_titulo]
    nota = valores_separados[coluna_rating]
    print(f"{titulo:30s}{nota:5s}")
