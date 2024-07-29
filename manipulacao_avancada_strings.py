# Esse arquivo mostra como fazer a manipulacao de strings

# Para pedir o input do usuario use a funcao input
# print("Digite seu nome")
# nome = input()

nome = "Mateus Oliveira"
print("Seu nome é ", nome)

# Use + para concatenar strings
primeiro_nome = "Mateus"
segundo_nome = "Oliveira"
print(primeiro_nome + " " + segundo_nome)

# Use * para repetir uma string
print("Eu estou rindo muito! ", "hau" * 10)

# Use strip() para remover os espaços iniciais e finais da string
nome_com_espacos = "          Mateus Oliveira             "
print(nome_com_espacos)
print(nome_com_espacos.strip())

# Para acessar um caractere qualquer da string use []
print("O primeiro caractere é", nome[0])

# Para acessar uma substring você pode usar o [inicio:fim]
print("O meu primeiro nome é", nome[:6])
print("O meu primeiro nome é", nome[0:6])

# Para acessar caractere você pode usar -1
print("O último caractere do nome é o", nome[-1])

# Com a funcao len() você pode saber o tamanho da string
print("O tamanho da string é ", len(nome))

# Deixar tudo minusculo com .lower() ou tudo maisculo com upper()
print(nome.lower())
print("AbCdEfG".lower())
print("AbCdEfG".upper())

# Pra contar quantas vezes aparece um substring você pode usar .count()
print("A quantidade de a's é ", nome.count("a"))

# Pra encontrar a posição de um caractere .find()
pos_espaco = nome.find(" ")
print("pos_espaco = ", pos_espaco)
print("O primeiro nome é ", nome[:pos_espaco])
print("O segundo nome é ", nome[pos_espaco + 1 :])

# O replace pode ser utilizado para substituir uma pedaco da string
novo_nome = nome.replace("Mateus", "Matias")
print(nome)
print(novo_nome)
