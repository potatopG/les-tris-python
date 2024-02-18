def tri_rapide(l):
    if len(l)<=1:
        return l
    else:
        l1,l2=[],[]
        pivot =l[-1]
        for i in range(len(l)-1):
            if l[i]<l[-1]:
                l1.append(l[i])
            else:
                l2.append(l[i])
        return tri_rapide(l1)+[l[-1]]+tri_rapide(l2)

def partition(T,debut,fin): 
#debut=c’est l’indice de départ de la liste T sur laquelle la fonction va travailler
#fin=  c’est l’indice qui indique l'élément final de la liste T 
    pivot = T[fin -1]
    k = debut    # place du 1er plus grand
    for i in range(debut,fin -1):
        if T[i] <pivot:
     	    T[i],T[k] =T[k],T[i] 
            k += 1
            T[fin -1],T[k] = T[k],T[fin -1]
     return k
def tri_rapide(t, d, f):
    if d < f:
        pivot = partition(t, d, f)
        tri_rapide(t, d, pivot)
        tri_rapide(t, pivot + 1, f)
    return t
