from collections import deque

palavras = input("Digite um conjunto de palavras: ")
lista = palavras.split()
fila = deque(lista)

print("Conjunto inicial:", fila)

for palavra in fila:
    if 'a' in palavra.lower():
        print(palavra)
