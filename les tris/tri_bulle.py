def tri_bubu(l):
    indice=0
    while indice<(len(l)-1):
        if l[indice+1]>l[indice]:
            l[indice],l[indice+1] = l[indice+1],l[indice]
            indice=0
        indice+=1
    return l

    

l=[3,5,7,4,2,6,1] 
print(tri_bubu(l))