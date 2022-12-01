"""
Ejercicio 8
Crea un programa que pida el número de palabras a introducir. Crear un diccionario de clave la palabra y
de valor la longitud de dicha palabra.
"""
n = int(input("Introduce el el número de palabras: "))
Dic = {}
for i in range(n):
    Palabras = str(input("Ingresa la palabra: "))
    Dic[Palabras] = len(Palabras)

print(Dic)