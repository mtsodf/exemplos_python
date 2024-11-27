times = ["Time A", "Time B", "Time C"]
pontuacoes = [10, 15, 20]


# for i in range(len(times)):
#    print(times[i], pontuacoes[i])

dicionario = {}
for time, pontuacao in zip(times, pontuacoes):
    print(time, pontuacao)

    dicionario[time] = pontuacao


print(dicionario)
