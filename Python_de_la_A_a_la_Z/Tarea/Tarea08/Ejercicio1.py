"""
Ejercicio 1
Crea un programa que pida un número entero positivo por teclado y que cree un diccionario cuyas claves
sean desde el número 1 hasta el número indicado. Los valores de cada clave serán las propias claves elevadas
al cubo.
"""

Lista = {}

n = int(input("Introduce un número entero positivo: "))

for i in range(1, n+1):
    Lista[i] = pow(i,3)

print(Lista)