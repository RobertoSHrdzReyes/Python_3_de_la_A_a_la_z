#Aprovechando el ejercicio de cumpleaños felíz, vamos a permitir 
#al usuario elegir a quien va sirigida la canción.
print("Indica el destinatario de la canción:")
name = input()

s1 = "¡Cumpleaños felíz!"
s2 = "Te deseamos todos"

song = (s1 + "\n") * 2 + s2.replace("todos",name) + ",\n" + s1

print(song)

