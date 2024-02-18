
def tri_rapide1(l):
    if len(l)<=1:
        return l
    else:
        l1,l2=[],[]#on cree deux listes vides qui dont les elements sont reparti en fonction de la valeur du pivot
        pivot =l[-1]
        for i in range(len(l)-1):
            if l[i]<l[-1]:
                l1.append(l[i])
            else:
                l2.append(l[i])
        return tri_rapide1(l1)+[l[-1]]+tri_rapide1(l2)#on fait appel a la fonction avec les deux listes l1 et l2 tout en tenant compte du pivot qui represente maintenant le milieu

def partition(T,debut,fin): #l'approche est differente puisque ici on reorganise la liste en fonction du pivot.elle est plus efficiente
    pivot = T[fin -1]
    k = debut    # place du 1er plus grand
    for i in range(debut,fin -1):
        if T[i] <pivot:
            T[i],T[k] =T[k],T[i] 
            k += 1
    T[fin -1],T[k] = T[k],T[fin -1]
    return k

def tri_rapide2(t, d, f):
    if d < f:
        pivot = partition(t, d, f)
        tri_rapide2(t, d, pivot)
        tri_rapide2(t, pivot + 1, f)
    return t

print(tri_rapide2([3,5,7,4,2,6,1]))
