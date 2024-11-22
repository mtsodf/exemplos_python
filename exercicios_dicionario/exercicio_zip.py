times = ["Time A", "Time B", "Time C"]
pontos = [10, 15, 20]

qtd_times = len(times)

time_pontos = {}

# for i in range(qtd_times):
# time_pontos[times[i]] = pontos[i]
# print(time_pontos)


for time, ponto in zip(times, pontos):
    time_pontos[time] = ponto

print(time_pontos)
