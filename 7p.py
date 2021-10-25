def listaNegativos(lista):
    prov = []
    for a in range(0,len(lista)):
        if lista[a]<0:
            prov.append(lista[a])
        else:
            continue
    return prov

LISTA = [1,3,-5,-1,-13,5,1,8,-4,7,-85]
print("La lista es:",LISTA)
LISTANEGAT = listaNegativos(LISTA)
print("La lista de los negativos es:",LISTANEGAT)