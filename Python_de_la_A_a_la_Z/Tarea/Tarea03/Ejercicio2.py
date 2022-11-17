#Ayuda a Pyratilla a crear un formulario donde se pida amablemente 
# el nombre, X
# la edad, X
# el hobby X
# y el sueño X 
# al interesado en formar parte de la tripulación del capitán Pyratilla. X

Nombre = input("Digita tu nombre:\n")
Edad = input("Digita tu edad:\n")
Hobby = input("Digita tu hobby:\n")
Dream = input("¿Cual es su sueño?\n")

print("Hola {} de {} años, cuyo hoby es {}, con el sueño de {}.\n ¡Seamos nakamas!".format(Nombre, Edad, Hobby.lower(), Dream.lower()))