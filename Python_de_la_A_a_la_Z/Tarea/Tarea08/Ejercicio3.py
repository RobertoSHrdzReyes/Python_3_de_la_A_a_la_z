"""
Ejercicio 3
Escribe un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar
el artículo y su precio por unidad. El artículo será la clave y el valor el precio, hasta que el usuario decida
terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente format
"""
Lista = {}
flag = 1
total = 0

while flag != 0:
    producto = str(input("Producto: "))
    precio = float(input("Precio: "))
    Lista[producto] = precio
    flag = 0 if input("si quiere terminar precione 0 sino precione enter\n") == "0" else 1

print("________________________")
for key in Lista:
    total += Lista[key]
    print(key," ",Lista[key])
print("Total: ",total)
print("________________________")
