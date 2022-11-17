"""
Pyratilla hizo un formulario para que los interesados en formar parte de su tripulación rellenaran y así 
poder evitarse más de una entrevista innecesaria.

Ahora es momento de filtrar las convocatorias:

    *El nombre debe empezar por mayúscula. Si es un nombre compuesto, entonces todos deben empezar por mayúscula.
    *La edad debe ser mayor o igual a 16 y menor o igual a 40.
    *El hobby indicado debe tener más de 10 caracteres.
    *La casilla del sueño no puede haber sido dejada en blanco.
"""
apellidoP, apellidoM = "a","b"

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingres tú edad: "))
hobby = input("Ingresa tu hobby: ")
dream = input("Ingresa tu sueño: ")

CC_nombre = nombre
CC_edad = edad
CC_hobby = hobby
CC_dream = dream

if nombre.find(" ") == -1:
    if nombre[0].isupper() == True:
        nombre = True
    else:
        nombre = False
else:
    nombre = nombre.split(" ")
    numero = len(nombre)
    if numero == 3:
        nombre1 = nombre[0]
        apellidoP = nombre[1]
        apellidoM = nombre[2]

        if (nombre1[0].isupper() == True) and (apellidoP[0].isupper() == True) and (apellidoM[0].isupper() == True):
            nombre = True
        else:
            nombre = False
    elif numero == 4:
        nombre1 = nombre[0]
        nombre2 = nombre[1]
        apellidoP = nombre[2]
        apellidoM = nombre[3]

        if (nombre1[0].isupper() == True) and (nombre2[0].isupper() == True) and (apellidoP[0].isupper() == True) and (apellidoM[0].isupper() == True):
            nombre = True
        else:
            nombre = False

if (edad >= 16) or (edad <= 40):
    edad = True
else:
    edad = False

if len(hobby) >= 10:
    hobby = True
else:
    hobby = False

if len(dream) == 0:
    dream = False
else:
    dream = True

if (nombre == True) and (edad == True) and (hobby == True) and (dream == True):
    print("El joven {} de {} de edad cuyo hobbye es {} y cuyo sueño es {} puede ser un candidato".format(CC_nombre,CC_edad,CC_hobby,CC_dream))
else:
    print("No cumple con los requisitos")