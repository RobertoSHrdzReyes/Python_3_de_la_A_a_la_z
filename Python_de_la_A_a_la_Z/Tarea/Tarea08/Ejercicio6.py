"""
Ejercicio 6
Crea un programa que permita al usuario introducir los nombres de los alumnos de una clase y las notas que
han obtenido. Cada alumno puede tener distinta cantidad de notas. Guarda la información en un diccionario
cuyas claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno.
1
El programa va a pedir el nombre de un estudiante e irá pidiendo sus notas (del 1 al 10) hasta que introduzcamos un 0. Al final, 
cuando el nombre que introduzcamos sea un string vacío, el programa nos mostrará la
lista de alumnos y la nota media obtenida por cada uno de ellos.
PISTA: Vas a necesitar la función sum().
"""
Nombre = " "
Cal = []
Lista = {}
Nota = 0

while True:
    Nombre = input("Agrega el nombre del alumno: ")
    if len(Nombre) != 0:
        Nota = int(input("Nota del alumno: "))
        while Nota != 0:
            Cal.append(Nota)
            Nota = int(input("Nota del alumno: "))
        else:
            Lista[Nombre] = Cal
            Cal = []
    else:
        break
    
print(Lista,"\n")
print("\nPromedios de los alumnos")
for key, val in Lista.items():
    print(key, ":", sum(val)/len(val))