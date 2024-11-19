numeros = ["zero", "um", "dois", "três"]

# numeros_dict = dict()

# for i, numero in enumerate(numeros):
#     numeros_dict[numero] = i


numeros_dict = {
    numero: i for i, numero in enumerate(numeros) if i % 2 == 0
}

print(numeros_dict)
