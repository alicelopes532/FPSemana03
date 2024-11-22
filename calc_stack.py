from collections import deque

numbers = input("Digite um conjunto de números: ")
lista = []
for number in numbers.split():
    lista.append(int(number))

conjunto = deque(lista)

print("Conjunto inicial:", conjunto)
while conjunto:
    numero = conjunto.pop()
    print(numero * 2)


