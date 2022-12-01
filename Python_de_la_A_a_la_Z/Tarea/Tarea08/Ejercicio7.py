"""
Ejercicio 7
Crea un programa que pida un número entero positivo por teclado y que cree un diccionario cuyas claves
sean desde el número 1 hasta el número indicado. Los valores de cada clave serán tantos símbolos "*" como
indique la clave.
"""
Dic = {}
n = abs(int(input("Introduce el numero de lementos: ")))

for i in range(1,n+1,1):
    Dic[i] = "*" * i

print(Dic)