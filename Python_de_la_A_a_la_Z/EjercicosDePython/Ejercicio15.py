#Dado un string, vamos a comprobar si contiene 
# espacios en blanco y, en caso de ser cierto, 
# concatenaremos cuántos tienen.
#PISTA: Investigar el operador in.
s = "Mi gato mola mucho"
c = " "
if c in s:
    print("El string tiene {} espacios en blanco".format(s.count(c)))