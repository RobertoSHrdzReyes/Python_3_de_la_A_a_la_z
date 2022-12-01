"""
Ejercicio 2
Escribe un programa que pregunte al usuario su nombre, edad y teléfono y lo guarde en un diccionario.
Después, debe mostrar por pantalla el mensaje ‘{nombre} tiene {edad} años y su número de teléfono es
{teléfono}.
"""
Lista = {}

Lista["nombre"] = str(input("¿Cúal es tu nombre?\n"))
Lista["edad"] = int(input("¿Cúal es tu edad?\n"))
Lista["telefono"] = int(input("¿Cúal es tu número de teléfono?\n"))

print("{} tiene {} años y número de teléfono {}".format(Lista["nombre"], Lista["edad"], Lista["telefono"]))