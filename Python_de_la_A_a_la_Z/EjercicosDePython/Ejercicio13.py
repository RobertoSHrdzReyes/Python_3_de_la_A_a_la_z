#Vamos a pedir al usuario plabras 
# o fraces y le vamos a devolver el mismo el mismo string modificado
#Con alguno de los métdos aprindidos según se indique:
# 1 Devolver la palabra en mayúscula X
# 2 devolver la frace con todas las palabras empezado en mayúsculas X
# 3 Devolver la palabra (con 3 o más letras) con todas las letras en
# minúscula salvo la tercera letra.X
# 4 Devolver la palabra con todas las letras en mayúsculas salvo
# la primera y la última.X
# 5 Devolver la frase donde cada vez que aparezcan las dos primeras 
# letras de la primera palabra, sean substituidas por cualesquiera 
# otras dos letras.

print("Intradusca una frace:")
Sentence = input()

print(Sentence.upper())

print(Sentence.title())

print(Sentence[:3].lower() + Sentence[3].upper() + Sentence[4:].lower())

print(Sentence[0].lower() + Sentence[1:(len(Sentence)-1)].upper() + Sentence[-1])

print(Sentence.replace(Sentence[:2],"hola"))
