"""
Questão 3: Contar Filmes, Séries e Mini Séries
Enunciado: Quantos registros são de filmes (movie), quantos são de séries de TV (tvSeries) e quantos são de minisséries (tvMiniSeries)?
"""

from questao01 import read_csv


def main():
    cabecalho, dados = read_csv("imdb_data.csv")

    coluna_tipo = cabecalho.index("type")
    coluna_tipo = 3

    num_filmes = 0
    num_miniseries = 0
    num_series = 0

    for dado in dados:
        tipo = dado[coluna_tipo]

        if tipo == "tvSeries":
            num_series += 1
        elif tipo == "movie":
            num_filmes += 1
        elif tipo == "tvMiniSeries":
            num_miniseries += 1
        else:
            print(f"Erro! Tipo {tipo} não esperado")

    print(f"O número de filmes é: {num_filmes}")
    print(f"O número de séries é: {num_series}")
    print(f"O número de miniséries é: {num_miniseries}")


if __name__ == "__main__":
    main()
