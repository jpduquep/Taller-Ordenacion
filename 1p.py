def eliminarRepetidos(lista):
    prov = [];
    rep = False;
    for a in lista:

        for x in prov:
            if a == x:
                rep = True
                break
            else:
                continue
        if(rep == False):
            prov.append(a)
        rep = False;
        print("Pasada",a,prov)
    return prov
        
Listax = [1,2,4,1,4,6,2,45,78,1,4,6,8,9,10]
print(Listax)
Listax = eliminarRepetidos(Listax)
print(Listax)