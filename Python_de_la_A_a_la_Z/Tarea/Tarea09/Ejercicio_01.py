"""
Ejercicio 1
Dado un número entero introducido por teclado, guarda sus divisores en un conjunto y muéstralo.
"""
numeros = set()
n = int(input("Introduce un numero: "))

for i in range(1, n+1):
    if i%2 == 0:
        numeros.add(i)

print(numeros)