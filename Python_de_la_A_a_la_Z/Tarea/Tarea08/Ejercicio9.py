"""
Ejercicio 9
Crea un programa que pida el número de palabras a introducir. Crear un diccionario de clave la palabra y
de valor el número de vocales de la palabra.
"""
Contador = 0
Dic = {}
Palabras = ""
n = int(input("Introduce el el número de palabras: "))
for i in range(n):
    Palabras = str(input("Ingresa la palabra: "))
    Palabras = Palabras.lower()
    for j in Palabras:
        if j == "a" or j == "e" or j == "i" or j == "o" or j == "u":
            Contador += 1
    Dic[Palabras] = Contador
    Contador = 0

print(Dic)