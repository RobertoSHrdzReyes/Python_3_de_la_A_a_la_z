#Vamos a hacer un programa que resuelva ecuaciones de primer grado de la forma Ax + B = 0
#Proporcionadas por el usuario donde A /= 0
A = float(input("Ingresa el coeficiente A\n"))
B = float(input("Ingresa el coeficiente B\n"))

if A != 0:
    sol = -B / A
    print("La solución es x = ",sol)
else:
    print("No hay ecuacuión que resolver, porque A es igual a 0.")
    