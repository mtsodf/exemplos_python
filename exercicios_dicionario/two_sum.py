import random
import time


def two_sum_lista(lista, alvo):

    for i, num in enumerate(lista):
        resto = alvo - num
        if resto in lista:
            j = lista.index(resto)
            if i != j:
                return i, j


def two_sum_dict(lista, alvo):
    esta_na_lista = {}
    for i, num in enumerate(lista):
        resto = alvo - num

        if resto in esta_na_lista:
            return i, esta_na_lista[resto]

        esta_na_lista[num] = i


lista = [10, 20, 40, 100]

lista = [random.randint(1, 39) for i in range(100000)]

start = time.time()
indices = two_sum_dict(lista, 80)
elapsed = time.time() - start
print(f"Tempo para cálculo {elapsed:.2f}")


start = time.time()
indices = two_sum_lista(lista, 80)
elapsed = time.time() - start
print(f"Tempo para cálculo {elapsed:.2f}")


if indices is not None:
    i, j = indices
    print(lista[i], lista[j])
else:
    print("Não existem dois número com a soma pedida")
