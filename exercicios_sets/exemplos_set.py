conjunto = {1, 2, 3}


print("O conjunto é ", conjunto)
print("A quantidade de elementos é", len(conjunto))


conjunto.add(-1)
print("O conjunto é ", conjunto)
print("A quantidade de elementos é", len(conjunto))

conjunto.add(2)
print("O conjunto é ", conjunto)
print("A quantidade de elementos é", len(conjunto))


conjunto.discard(10)
print("O conjunto é ", conjunto)
print("A quantidade de elementos é", len(conjunto))

num = conjunto.pop()
print("Foi removido o ", num)
print("O conjunto é ", conjunto)
print("A quantidade de elementos é", len(conjunto))
