"""Crie um jogo de batalha naval onde o computador sorteia um local do barco e o usuário deve tentar acertar onde está o barco."""

from batalha_naval_utils import sortear_barcos, imprimir_tabuleiro, pegar_palpite_do_usuario, posicao_esta_em_um_barco


def main():
    tamanho_do_barco = 5
    palpites = []
    barcos = sortear_barcos(tamanho_do_barco)

    num_acertos = 0

    while num_acertos < tamanho_do_barco:

        imprimir_tabuleiro(palpites, barcos)
        palpite = pegar_palpite_do_usuario(palpites)

        print(palpites)

        if posicao_esta_em_um_barco(palpite, barcos):
            num_acertos += 1

    if num_acertos == tamanho_do_barco:
        print("Parabéns! Você venceu o jogo")


if __name__ == "__main__":
    main()
