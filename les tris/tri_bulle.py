def tri_bubu(l):
    indice=0
    while indice<(len(l)-1):
        if l[indice+1]>l[indice]:
            l[indice],l[indice+1] = l[indice+1],l[indice]
            indice=0
        indice+=1
    return l

    

#deuxieme methode

def tri_bulle(l):
    verif=True                                                   
    while verif:
        verif=False
        for k in range(1,len(l)):
            if l[k]<l[k-1]:
                l[k], l[k - 1] = l[k - 1], l[k]
                verif =True                                                 
    return l

