#Escribir un programa que lea un entero positivo, n, 
# introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. 
# La suma de los  primeros enteros positivos puede ser calculada de la siguiente forma:

n = int(input("Introduce un número: "))
Suma= n*(n+1)/2
print("La suma de todos los número de 1 hasta "+str(n)+" es: "+str(Suma))
