def ordenamientoBurbuja(unaLista):
    contador = 1; #Contador de for
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp
        print("Bubble Pasada",contador,unaLista)
        contador +=1;

def ordenamientoInsercion(A):
    for i in range(len(A)):
        for j in range(i,0,-1):
            if(A[j-1] > A[j]):
                aux=A[j];
                A[j]=A[j-1];
                A[j-1]=aux;
        print("Insercion Pasada",i+1,A)

def ordenamientoSelectivo(lista):
    for x in range (0,len(lista)-1):
        menor = lista[x]
        indice = x
        for y in range(x+1,len(lista)):
            if lista[y] < menor:
                menor = lista[y]
                indice = y
        lista[indice] = lista[x]
        lista[x] = menor;
        print("Selectivo Pasada",x+1,lista)

listaX = [47,3,21,32,56,92]
ordenamientoBurbuja(listaX)
ordenamientoInsercion(listaX)
ordenamientoSelectivo(listaX)

