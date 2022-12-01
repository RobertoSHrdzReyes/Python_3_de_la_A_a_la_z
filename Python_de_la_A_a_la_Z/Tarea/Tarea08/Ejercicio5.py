"""
Ejercicio 5
Crea un programa que lea números enteros hasta que introduzca el 0 y devuelva un diccionario con la
cantidad números pares e impares introducidos.
"""
Lista = {}
n = 1

contador_par = 0
contador_inpar = 0
while n != 0:
    n = float(input("Intriduce un número: "))
    if n == 0:
        contador_par += 0
    elif n % 2 == 0:
        contador_par += 1
    else:
        contador_inpar += 1

Lista = dict(NumperosPares = contador_par, NumerosImpares =  contador_inpar)
print(Lista)