#Vamos a pedirle al usuario su año de nacimieto 
# y el año actual 
# y le vamos a imprimir por pantlla su edad.
print("Digita tú año de nacimieto")
AnoDeNacimiento = int(input())

print("Digita el año actual")
AnoActual = int(input())

Edad = AnoActual - AnoDeNacimiento

print("Tu edad es: " + str(Edad))