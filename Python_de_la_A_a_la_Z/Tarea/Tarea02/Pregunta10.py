# Con lo hecho en los ejercicios 6, 7, 8 y 9, imprime por pantalla todos los datos introducidos por el usuario
# tal y como se muestra en el siguiente ejemplo, donde el usuario ha indicado que su nombre es María; su
# apellido, Santos; su edad, 21; y su ciudad, Palma de Mallorca.
# Su nombre es María Santos, tiene 21 años y actualmente vive en Palma de Mallorca.

nombre = input("Digita tu nombre:\n")
apellido = input("Digita tu apellido:\n")
edad = input("Digita tu edad:\n")
ciudad = input("Digita tu ciudad:\n")

print("Su nombre es {} {}, tiene {} años y actualmente vive en {}".format(nombre, apellido, edad, ciudad))