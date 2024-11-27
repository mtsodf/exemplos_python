# Primeira maneira de ler o arquivo

print("-" * 40)
print("Leitura com read()")
print("-" * 40)
arquivo = open("alunos.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()


print("")
print("-" * 40)
print("Leitura com readlines()")
print("-" * 40)
arquivo = open("alunos.txt", "r")
conteudo = arquivo.readlines()
print(conteudo)
arquivo.close()

print("")
print("-" * 40)
print("Leitura com readline()")
print("-" * 40)
arquivo = open("alunos.txt", "r")
conteudo = arquivo.readline()

while conteudo:
    print(conteudo.rstrip())
    conteudo = arquivo.readline()

arquivo.close()
