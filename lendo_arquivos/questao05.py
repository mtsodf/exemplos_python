import questao01


def media_lista(lista):
    media = sum(lista)
    media /= len(lista)
    return media


cabecalho, dados = questao01.read_csv("imdb_data.csv")

print(cabecalho)

col_nome = cabecalho.index("title")
col_tipo = cabecalho.index("type")
col_nota = cabecalho.index("averageRating")


def imprimir_midias_acima_da_media(tipo_da_midia="movie"):
    notas_filmes = []

    for dado in dados:
        tipo = dado[col_tipo]

        if tipo == tipo_da_midia:
            titulo = dado[col_nome]
            nota = float(dado[col_nota])
            notas_filmes.append(nota)

    media_notas_filmes = media_lista(notas_filmes)
    print(f"A média das notas é: {media_notas_filmes}")

    filmes_acima_da_media = [
        (float(dado[col_nota]), dado[col_nome])
        for dado in dados
        if float(dado[col_nota]) > media_notas_filmes and dado[col_tipo] == tipo_da_midia
    ]
    filmes_acima_da_media.sort()

    for filme in filmes_acima_da_media[-30:]:
        print(filme)


imprimir_midias_acima_da_media("movie")
imprimir_midias_acima_da_media("tvSeries")
imprimir_midias_acima_da_media("tvMiniSeries")
