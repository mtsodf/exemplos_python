""""
Faça um programa que dado três números encontra qual é o maior deles
"""

num0 = float(input("Digite um número:\n"))
num1 = float(input("Digite um número:\n"))
num2 = float(input("Digite um número:\n"))


if num0 >= num1 and num0 >= num2:
    print(f"O maior número é o {num0}")
elif num1 >= num0 and num1 >= num2:
    print(f"O maior número é o {num1}")
else:
    print(f"O maior número é o {num2}")


print("Fim!")
