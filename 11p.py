def quick_sort(lista):
    izquierda = []
    derecha = []
    centro=[]

    if len(lista) >1:
        pivote = lista[-1]
        for i in lista:
            if i<pivote:
                izquierda.append(i)
            elif i==pivote:
                    centro.append(i)
            else:
                    derecha.append(i)
        return quick_sort(izquierda) + centro + quick_sort(derecha)
    else:
        return lista

a = [4,1,5,2,8,54,1,3,5,54,13,2,5,7,25,67,43,3,34,36,87,65,43,22,13] #lista A con 100 elementos
b = [4,4,4,1,3,2,7,87,12,15,17,4,32,12,16,19,21,23,7,8,5,9] #lista B con 60 elementos

#Punto A
a = quick_sort(a);
print(a)
b = quick_sort(b);
print(b)

#Punto B
c = a + b 
print(c)

#Punto C
c = quick_sort(c)
print(c)