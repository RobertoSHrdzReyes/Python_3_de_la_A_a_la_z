"""
Ejercicio 1
Haz que un usuario introduzca un número real
y evalúa si dicho número es positivo, 
negativo o cero.
Devuelve
por pantalla el resultado en cada caso.


Numero = int(input("Digita un número real: "))

if Numero > 0:
	print("El número "+str(Numero)+" es positivo")
elif Numero < 0:
	print("El número "+str(Numero)+" es negativo")
else:
    print("El número es 0")

===========================================================================================================
Ejercicio 2
Haz que un usuario introduzca su nombre
y evalúa con operadores if y else si dicho nombre tiene una longitud mayor a 10 caracteres o no. 
Devuelve por pantalla el resultado en cada caso.


nombre = input("Digita tu nombre: ")

NumeroDeCaracteres = len(nombre)

if NumeroDeCaracteres > 10:
    print("El Nombre tiene más de 10 caracteres")
else:
    print("El Nombre no tiene más de 10 caracteres")

===========================================================================================================
Ejercicio 3
Realiza el ejercicio anterior con el uso del operador ternario.

nombre = input("Digita tu nombre: ")

NumeroDeCaracteres = len(nombre)

print("El Nombre tiene más de 10 caracteres") if NumeroDeCaracteres > 10 else print("El Nombre no tiene más de 10 caracteres")

=============================================================================================================
Ejercicio 4
Haz que un usuario introduzca dos números enteros positivos.
Comprueba si el primer número introducido por el usuario es mayor o igual que el segundo número introducido por el usuario. Devuelve por pantalla el
resultado en cada caso.
PISTA: Asegúrate de hacer uso de la función int() donde pertoque.

N1 = abs(int(input("Digita un número: ")))
N2 = abs(int(input("Digita otro número: ")))

if N1 > N2:
	print("{} > {}".format(N1,N2))
elif N1 == N2:
	print("{} = {}".format(N1,N2))
else:
	print("{} < {}".format(N1,N2))
===========================================================================================================
Ejercicio 5
Haz que un usuario introduzca dos números enteros positivos. 
Suponiendo que el primer número introducido por el usuario es mayor o igual al segundo número introducido por el usuario, 
comprueba que la división del primer número entre el segundo número es exacta.
En caso de la división ser exacta, devuelve el cociente por pantalla e indica que la división en efecto es exacta.
En caso de la división no ser exacta, devuelve el cociente y el resto por pantalla e indica que la división entre los dos números no es exacta

N1 = abs(int(input("Digita un número: ")))
N2 = abs(int(input("Digita otro número: ")))

if N1 >= N2:
   if N1 % N2 == 0:
       print("La divición es exacta")
       print(N1 // N2)
   else:
       print("La divición no es exacta")
       print(str(N1 // N2) + ", " + str(N1 % N2))
==================================================================================================================
Ejercicio 6
Fusiona lo hecho en los ejercicios 4 y 5 para que
1. Un usuario introduzca dos números enteros por pantalla.
2. Comprobar si el primer número es mayor o igual al segundo número introducido por el usuario. 
Devolver por pantalla en que caso nos encontramos.
3. Hacer la división entera pertinente en cada caso.
4. Si la división es exacta, entonces devolver por pantalla el cociente e indicar que la división es exacta.
Si la división no es exacta, entonces devolver por pantalla el cociente y el resto e indicar que la división
realizada no es exacta.

N1 = abs(int(input("Digita un número: ")))
N2 = abs(int(input("Digita otro número: ")))


if N1 > N2:
	print("N1 > N2")
	if N1 % N2 == 0:
	    print("La división es exacta")
	    print(N1 // N2)
	else:
		print("La división no es exacta")
		print(str(N1 // N2) + ", " + str(N1 % N2))

	
elif N1 == N2:
	print("N1 = N2")
	if N1 % N2 == 0:
	    print("La división es exacta")
	    print(N1 // N2)
	else:
		print("La división no es exacta")
		print(str(N1 // N2) + ", " + str(N1 % N2))

=================================================================================================================
Ejercicio 7
Haz que un usuario introduzca dos números enteros positivos. Comprueba si el mayor es múltiplo del menor.
Devuelve por pantalla el resultado en cada caso.

N1 = abs(int(input("Digita un número: ")))
N2 = abs(int(input("Digita otro número: ")))

if N1 > N2:
	if N1 % N2 == 0:
		print("{} es múltiplo de {}".format(N1,N2))
elif N1 < N2:
	if N2 % N1 == 0:
		print("{} es múltiplo de {}".format(N2,N1))
=====================================================================================================================
Ejercicio 8
Haz que un usuario introduzca una palabra y comprueba si dicha palabra empieza por mayúscula. Devuelve
por pantalla el resultado en cada caso.
"""
"""
palabra = input("Introduce una palabra: ")
if palabra[0].isupper() == True:
	print("La palabra comienza con mayúsculas")
else:
	print("La palabra no comienza con mayúsculas")
"""
"""
Ejercicio 9
Haz un usuario introduza una letra y comprueba si se trata de una vocal. Si el usuario introduce un string
de más de un carácter, infórmale de que no se puede procesar el dato, pues debe tener como máximo tamaño
1.
PISTA: Convierte la letra introducida a minúsculas para tener que realizar menos comprobaciones
"""
"""
letra = input("Introduce una letra: ")
print(len(letra))

if len(letra) > 1:
	print("No sepuede procesar el dato")

else:
	letra = letra.lower()

	if  letra.startswith("a") == True:
		print("La letras es una vocal")
	elif  letra.startswith("e") == True:
		print("La letras es una vocal")
	elif  letra.startswith("i") == True:
		print("La letras es una vocal")
	elif  letra.startswith("o") == True:
		print("La letras es una vocal")
	elif  letra.startswith("u") == True:
		print("La letras es una vocal")
	else:
		print("La letras es una consonante")
"""
from math import sqrt


print("Resolviendo ecuaciones de segundo grado")
a = float(input("Digite el valor de A: "))
b = float(input("Digite el valor de B: "))
c = float(input("Digite el valor de C: "))

if a == 0:
	print("La funcion de segundo orden no tiene solución")

else:
	delta = pow(b,2) - (4 * a * c)
	if delta > 0:
		x1 = (-b + sqrt(delta))/(2 * a)
		x2 = (-b - sqrt(delta))/(2 * a)
		print("La función tiene dos soluciones distintas")
		print("Los resultados son x1 = {}, x2 = {}".format(x1,x2))
	elif delta == 0:
		x = -b/(2 * a)
		print("La función tiene dos soluciones iguales")
		print("El resultado es x = " + str(x))
	elif delta < 0 :
		print("No existe solución") 
