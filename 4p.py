def shell_sort(inp, n):
    h = n // 2
    contadorh = 1; #Efecto practico de ejercicio
    while h > 0:
        contadori = 1; #Efecto practico de ejercicio
        for i in range(h, n):
            
            t = inp[i]
            j = i
            while j >= h and inp[j - h] > t:
                inp[j] = inp[j - h]
                j -= h
            inp[j] = t
            print("       Subpasada No.",contadori,inp)
            contadori +=1;
        print("Pasada No.",contadorh,inp) #Efecto practico de ejercicio
        contadorh += 1; #Efecto practico de ejercicio
        h = h // 2
        


lista = [8, 43, 17, 6, 40, 16, 18, 97, 11, 7]
n = len(lista)
print(lista)
shell_sort(lista, n)
print(lista)