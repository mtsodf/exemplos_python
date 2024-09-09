"""
Escreva um programa que peça ao usuário um número, n. Em seguida, use o programa deve imprimir repetidamente uma mensagem. Por exemplo, se o usuário inserir 99, seu programa deverá imprimir isto:

99 books on Python on the shelf 99 books on Python
Take one down, pass it around, 98 books left.
98 books on Python on the shelf 98 books on Python
Take one down, pass it around, 97 books left.
...
1 book on Python on the shelf 1 book on Python 
Take one down, pass it around, no more books!
"""

n = 99

for i in range(n, 0, -1):

    if i == 1:
        print(f"{i} book on Python on the shelf {i} on Python")
        print("Take one down, pass it around, no more books!")
    else:
        print(f"{i} books on Python on the shelf {i} on Python")
        if i - 1 == 1:
            print(f"Take one down, pass it around, {i-1} book left.")
        else:
            print(f"Take one down, pass it around, {i-1} books left.")
