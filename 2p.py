def eliminarRepetidosOrden(listaOrd):
    numeroProv = listaOrd[0]
    prov = [listaOrd[0]]
    for a in range(1,len(listaOrd)-1):
        if listaOrd[a] == numeroProv:
            continue
        else:
            prov.append(listaOrd[a])
        numeroProv = listaOrd[a]
    return prov;

Listax = [1,1,1,2,4,6,7,8,8,9,10,12,12,13,14,15,15,15,15]
print(Listax)
Listax = eliminarRepetidosOrden(Listax)
print(Listax)