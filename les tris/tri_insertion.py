def tri_insertion(l):
    for i in range(1,len(l)):#on parcourt la liste à partir du deuxieme élément
        j=i
        while j>0 and l[j-1]>l[j]:#on compare l'element j avec l'element j-1
            l[j],l[j-1]=l[j-1],l[j]#si j est plus grand que j-1 alors on sort de la boucle
            j-=1
    return l

      
#methode recursive

def insere(t,j): 
      if j>0 and t[j]<t[j-1]:#tant que le-j-eme element est plus grand que le j-1-eme alors on rentre pas dans une boucle recursive 
        t[j-1],t[j]=t[j],t[j-1]
        insere(t,j-1)
# Insère t[j] dans la tranche t[:j−1]  #supposée triée
def tri_ins(t,j=1):#j =1 car on commence a partir du deuxieme element
    if j<len(t):
      insere(t,j) 
      tri_ins(t,j+1)#boucle recursive
    return t
