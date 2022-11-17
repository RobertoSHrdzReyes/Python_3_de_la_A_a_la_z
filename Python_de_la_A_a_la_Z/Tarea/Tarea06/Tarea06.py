"""
Ejercicio 1
Haz que el usuario introduzca números enteros por teclado. Mientras el usuario no introduzca el 0, muestra
si el número introducido es par o impar.
"""
"""
n = int(input("Introduce el primer número: "))
if n % 2 == 0:
    print("El número es par.\n")
else:
    print("El número es inpar.\n")

while n != 0:
    n = int(input("Introduce un número: "))
    if n == 0:
        break
    elif n % 2 == 0:
        print("El número es par.\n")
    else:
        print("El número es inpar\n")
else:
    print("el número es 0")
"""

"""
Ejercicio 2
Haz que el usuario introduzca una palabra y una letra por teclado. Comprueba si la palabra contiene la
letra o no e indícaselo al usuario por pantalla.
"""
"""
Palabra = input("Introduce una palabra: ")
letra = input("Agrega una letra: ")
contador = 0

Palabra = Palabra.lower()

for c in Palabra:
    if c == letra:
        contador += 1

if contador == 0:
    print("la letra no se encuentra en la palabra")
else:
    print("La letra ",letra, " aparece ",contador, " veces")
"""

"""
Ejercicio 3
Haz que el usuario introduzca precios por teclado (si introduce 0, entonces es que ha finalizado). Si el usuario
pasa de 200€, entonces ya no debe poder introducir más precios pues se ha pasado de presupuesto. Sea cual
sea el resultado (o bien el precio final o bien que no tiene más presupuesto), indícaselo por pantalla al usuario.
"""
"""
precio = 1
contador = 0

while precio != 0:
    precio = float(input("Introduce el precio del producto: "))
    contador += precio

    if precio == 0 or contador >= 200:
        break

if precio == 0:
    print("La cuenta fue de $",contador)
elif contador >= 200:
    print("Se a quedado sin presupuesto, le faltan $"+ str(contador - 200))
"""
"""
Ejercicio 4
Haz que el usuario introduzca números enteros por teclado. Mientras el usuario no introduzca el 0, calcula
cuántos números positivos y cuántos negativos ha introducido y muéstraselo al final.
"""
"""
n = 1
contador_p = 0
contador_n = 0

while n != 0:
    n = int(input("Introdusca un número: "))
    if n == 0:
        break
    elif n > 0:
        contador_p += 1
    elif n < 0:
        contador_n += 1
print("huvo {} números positivos y {} número negativos".format(contador_p, contador_n))
"""
"""
Ejercicio 5
Haz que el usuario introduzca números por teclado. Mientras el usuario no introduzca el 0, pídele otro
número. Cuando el usuario introduzca el 0, muéstrale la media aritmética de los números que ha introducido.
"""
"""
n = 1
contador = 0
i = 0
while n != 0:
    n = int(input("introduzca un número: "))
    if n == 0:
        break
    contador += n
    i += 1
contador = contador/i
print("La media aritmética es "+str(contador))

"""
"""
Ejercicio 6
Haz que el usuario introduzca dos números enteros por teclado. El primero será el extremo izquierdo del
intervalo y, el segundo, el extremo derecho. Imprime todos los números que se encuentren entre los dos
números introducidos por el usuario (los extremos incluidos).
"""
"""
print("Todos los número dentro de un rango")
n1 = int(input("Introduce un número: "))
n2 = int(input("Introduce un número: "))

for c in range(n1+1, n2):
    print(c)

"""
"""
Ejercicio 7
Haz que el usuario introduzca dos números enteros por teclado. El primero será el extremo izquierdo del
intervalo y, el segundo, el extremo derecho. Imprime la suma de todos los múltiplos de 3 que se encuentren
entre los dos números introducidos por el usuario (los extremos incluidos). Finalmente, muestra por pantalla
el resultado de la suma.
"""
"""
n1 = int(input("Introduce un número: "))
n2 = int(input("Introduce un número: "))
contador = 0
for c in range(n1, n2+1):
    if c % 3 == 0:
        contador += c

print("La suma de todos los múltiplos de 3 precentes es: ",contador)
"""
"""
Ejercicio 8
Pídele al usuario cuántos números va a introducir. Con un bucle for, solicítale esa cantidad de números y
calcula su producto.
"""
"""
n = int(input("¿Cúantos números quiere introducir? "))
producto = 1
for c in range(1, n+1):
    numeros = int(input("Digita un un número: "))
    producto = producto * numeros

print("El producto es ",producto)
"""
"""
Ejercicio 9
Haz que el usuario introduzca su edad y el año actual. Imprime todos los años que han pasado desde su año
de nacimiento hasta el año actual (ambos incluidos).
"""
"""
edad = int(input("Introduce tu edad: "))
year = int(input("Introduce el año actual: "))

born = year - edad

for c in range(born, year + 1):
    print(c)

"""
"""
Ejercicio 10
Haz que el usuario introduzca un número entero. Muestra un cuadrado y luego un triángulo rectángulo de
lado y altura, respectivamente, el número entero introducido. Por ejemplo, si el usuario introduce como
número 5, se deberá mostrar:
*          * * * * *
* *        * * * * *
* * *      * * * * *
* * * *    * * * * *
* * * * *  * * * * *
"""
i = 1
n = int(input("Indíca el número de niveles: "))
j = (2 * n) - 1
while i <= n:
    print(("* "*i)+(" "*j)+("* "*n))
    i += 1
    j -= 2