def busquedaMatriz(Matriz,num):
    encontrado = False;
    for fila in range(0,len(Matriz)):
        for columna in range(0,len(Matriz[fila])):
            if(Matriz[fila][columna]) == num:
                encontrado = True;
            else:
                continue;
    if encontrado == False:
        return "no"
    else:
        return "si"


Matriz = [[1,2,2,2,3,4],[1,2,3,3,4,5],[3,4,4,4,4,6],[4,5,6,7,8,9]]
for a in range(0,len(Matriz)):
    print(Matriz[a])
n = int(input("¿Que numero desea buscar? /"))
print("El elemento", n, busquedaMatriz(Matriz,n),"fue encontrado")