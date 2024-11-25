carros = {"Fusca": 1970, "Civic": 2019, "Gol": 2015, "Celta": 2015}


for nome_carro in carros.keys():
    ano_fabricacao = carros[nome_carro]
    print(nome_carro, ano_fabricacao)


print("\n", "-" * 30, "\n")

for nome_carro, ano_carro in carros.items():
    print(nome_carro, ano_fabricacao)


print("\n", "-" * 30, "\n")

for carro in carros.items():
    print(carro[0], carro[1])
