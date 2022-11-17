#Del string s del ejercicio anterior, obtén el substring chocolate y guárdalo en una variable 
# llamada s_sub.
#No vale contar, deberás hallar los índices del substring con el método .find() 
# (o el que mejor consideres) ya función len().
#Finalmente, imprime tu resultado por pantalla
s = "Mi pasión por el chocolate es superior a mis fuerzas"
s_sub = s[(s.find("c") - 1):]
s_sub = s_sub[:(s_sub.find("e") + 1)]
print(s_sub)
