def ganadorElecciones(listaVotos):
    mayor = 0;
    Electorales = [];
    for a in range(0,len(listaVotos)):
        if listaVotos[a]>mayor:
            mayor = listaVotos[a]

    for b in range (0,mayor+1):
        Electorales.append([b,0])
    #print(Electorales)       #Creacion de candidatos y sus votos

    for c in range(0,len(listaVotos)):
        r = listaVotos[c]
        Electorales[r][1] +=1;
    #print(Electorales)      #Suma de votos de candidatos
    
    indiceMayor = 0;
    vot = Electorales[0][1]
    for d in range(1,len(Electorales)):
        if Electorales[d][1] > vot:
            indiceMayor = d;
            vot = Electorales[d][1]
    print("Ha ganado el candidato",indiceMayor,"con un total de",vot,"votos")
        
votos = [1,2,3,2,1,3,2,4,2,4,5,3,4,5,3,1,2,4,3,5,4,1,2,3,4,1,2,4,2,5,5,5,0,0]
ganadorElecciones(votos);
