# Programa para verificar se um triângulo é valido

# O triangulo terá lados a, b e c.
a = int(input("Digite o primeiro lado do triângulo:\n"))
b = int(input("Digite o segundo lado do triângulo:\n"))
c = int(input("Digite o terceiro lado do triângulo:\n"))

print("\n")

# Testar se os lados foram um triangulo
if (a + b > c) and (a + c > b) and (b + c > a):

    print(f"Os lados {a}, {b} e {c} formam um triângulo!!")

    if a == b and b == c:
        print("O triângulo é equilátero")
    elif (a == b) or (a == c) or (b == c):
        print("O triângulo é isósceles")
    else:
        print("O triângulo é escaleno")

else:
    print(f"Os lados {a}, {b} e {c} NÃO formam um triângulo!!")
