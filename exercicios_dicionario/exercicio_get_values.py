def get_values(dicionario, chave, valor_padrao=None):
    if chave in dicionario:
        return dicionario[chave]
    else:
        return valor_padrao


dicionario = {"a": 1, "b": 2, "c": 3}


print(get_values(dicionario, "a"))

print(get_values(dicionario, "m", "m não encontrado"))


print(dicionario.get("m"))

print(dicionario["m"])
