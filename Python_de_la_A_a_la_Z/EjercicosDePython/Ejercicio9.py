c = float(input("Ingresa el capital inicial "))
i = float(input("Ingresa tu tasa de interes en decimales "))
t = float(input("Ingresa el número de años a invertir "))
CapitalOntenido = round(c*(i/100+1)**t,2)
print("El capital obtenido es de $"+str(CapitalOntenido)+" (MXN)")