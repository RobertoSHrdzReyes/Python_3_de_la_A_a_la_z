#Escribir un programa que pida al usuario 
#dos números enteros y muestre por pantalla 
#la <n> entre <m> da un cociente <c> y un resto
#<r> donde <n> y <m> son los números introducidos
#por el usuario, y <c> y <r> son el cociente y el 
#resto de la división entera respectivamente.

n = int(input("Ingresa el primer número entero: "))
m = int(input("Ingresa el segundo número entero: "))
c = int(n/m)
r = int(n%m)
print(n," entre ",m," da un cociente de ",c," y un residuo de ",r)

