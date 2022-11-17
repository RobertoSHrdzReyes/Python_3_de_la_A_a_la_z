#Vamos a comprobar si un número es par o inpar haciendo uso del operador ternario
n = int(input("Digita un número: "))
message = "El número es par" if n % 2 == 0 else  "El número es inpar"
print(message)