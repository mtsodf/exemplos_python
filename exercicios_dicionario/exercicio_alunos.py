notas_dict = {
    "Ana": [9, 8, 10],
    "João": [7, 6, 8],
    "Maria": [10, 9, 9],
    "Lucas": [6, 5, 7],
}

notas_media = {}

for nome, notas in notas_dict.items():
    notas_media[nome] = sum(notas) / len(notas)


for nome in notas_media:
    media = notas_media[nome]
    print(f"{nome:10s} {media:5.2f}")


media_turma = sum(notas_media.values()) / len(notas_media)

print(f"A média da turma é {media_turma:.2f}")
