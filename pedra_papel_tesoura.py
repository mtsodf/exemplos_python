import random

# Jogada aleatória do computador
cpu_escolha = random.choice(["pedra", "papel", "tesoura"])
jogador_escolha = input("Digite sua jogada (pedra, papel ou tesoura)\n")
print(f"Computador jogou {cpu_escolha}")

# Caso do empate
if cpu_escolha == jogador_escolha:
    print("EMPATE!!!!!!!")
# Vitória do jogador
elif (
    (jogador_escolha == "pedra" and cpu_escolha == "tesoura")
    or (jogador_escolha == "papel" and cpu_escolha == "pedra")
    or (jogador_escolha == "tesoura" and cpu_escolha == "papel")
):
    print("Jogador Ganhou!!! Festa!! Parabéns")
# Vitória da CPU
else:
    print("Perdeu!! É uma pena. Tente mais uma vez. Não desista!")
