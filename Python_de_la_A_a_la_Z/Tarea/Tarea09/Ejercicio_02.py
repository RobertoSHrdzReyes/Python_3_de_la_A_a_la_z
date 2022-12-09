"""
Ejercicio 2
Crea un programa que dado un conjunto, nos devuelva su mínimo. Debes hacerlo sin recurrir a la función
min().
"""
numeros = {1,20, 35, 10,-4,15,-5,-100}
min = 9999
for i in numeros:
    if i < min:
        min = i

print(min)