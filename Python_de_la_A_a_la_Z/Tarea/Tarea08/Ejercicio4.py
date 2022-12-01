"""
Ejercicio 4
Crea un programa que lea números enteros hasta que introduzca el 0 y devuelva un diccionario con la
cantidad números positivos y negativos introducidos.
"""
Lista = {}
n = 1
contador_positivo = 0
contador_negativo = 0
while n != 0:
    n = float(input("Introduce un número "))
    if n >= 1:
        contador_positivo += 1
    elif n <= -1:
        contador_negativo += 1

Lista = dict(nuperosPositivos = contador_positivo, numerosNegativos = contador_negativo)
print(Lista)