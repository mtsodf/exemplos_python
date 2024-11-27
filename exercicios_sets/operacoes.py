A = {1, 2, 3, 4}

# B = {i for i in range(3, 11)}

B = set()
for i in range(3, 11):
    B.add(i)


print(f"A = {A}")
print(f"B = {B}")

A_uniao_B = A | B
A_uniao_B = A.union(B)

print("A união é", A_uniao_B)

A_intersecao_B = A & B
A_intersecao_B = A.intersection(B)

print("A interseção é", A_intersecao_B)


print("A - B é", A - B)

print("B - A é", B.difference(A))


if 10 in A:
    print("10 está no A")
else:
    print("10 não está no A")

if 10 in B:
    print("10 está no B")
else:
    print("10 não está no B")
