nome = "Érika"
idade = 35

# Para criar uma f-string basta colocar um f antes das aspas
# Dentro da f-string você pode colocar variáveis entre chaves
print(f"Meu nome é {nome} e tenho {idade} anos.")


# Você pode fazer operações dentro das chaves
print(f"Daqui a 10 anos terei {idade + 10} anos.")

# Você pode chamar funções dentro das chaves
print(f"Meu nome em maiúsculas é {nome.upper()}.")
print(f"Meu nome em minúsculas é {nome.lower()}.")
print(f"Meu nome tem {len(nome)} letras.")

# Você pode formatar um número float com um número específico de casas decimais
import math

print(f"O valor de pi é {math.pi:.2f}.")

# Você pode alinhar o texto
print(f"{'esquerda':<20s} {'direita':>20s} {'centro':^20s}")

# Você pode escrever um inteiro com zeros à esquerda
print(f"O número 42 com zeros à esquerda é {42:05d}.")


# Você pode criar uma tabela alinhada
print(f"{'Nome':<15} {'Idade':<10s} {'Cidade':<20}")
print(f"{'Mateus':<15} {25:<10d} {'São Paulo':<20}")
print(f"{'Érika':<15s} {35:<10d} {'Sobral':<20}")
print(f"{'Matias':<15s} {30:<10d} {'Fortaleza':<20}")
