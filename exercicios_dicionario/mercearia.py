# Ele vai associar os produtos com seus preços em reais
supermercado = {"leite": 7.88, "ovos": 12.00, "pão francês": 1.00}


print(supermercado)


# Acessando um valor do dicionário
print(supermercado["pão francês"])


# Adicionando uma nova dupla chave:valor no dicionário
supermercado["coca-cola"] = 4.00

print(supermercado)

# Pra modificar um valor
supermercado["leite"] = 6.00
print(supermercado)


# Dar um desconto de 20% no preço dos ovos
supermercado["ovos"] *= 0.8
print(supermercado)


# Deletando uma chave específica do dicionário
# supermercado.pop("pão francês")
del supermercado["pão francês"]
print(supermercado)


# Iterar sobre os produtos

print("-" * 60)
print("Produtos".center(60))
print("-" * 60)
for produto in supermercado.keys():
    print(f"{produto:20s} {supermercado[produto]:15.2f}")


for preco in supermercado.values():
    print(preco)
