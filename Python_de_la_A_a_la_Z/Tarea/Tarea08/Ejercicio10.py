A = [[1,2,3,4],[0,2,4,6],[4,3,2,1]]
info = {"filas":len(A),
        "Columnas":len(A[0])}
    
for i in range(len(A)):
    info["filas" + str(i)] = A[i]

print(info)