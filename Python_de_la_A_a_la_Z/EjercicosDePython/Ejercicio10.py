#Vamos a convinar concatenación y repeticion de strings para reproducir la canción "Cumpleaños felíz".
s1 = "¡Cumpleaños felíz!"
s2 = "Te deceamos todos"


song = (s1 + "\n") * 2 + s2 + ",\n" + s1
print(song)