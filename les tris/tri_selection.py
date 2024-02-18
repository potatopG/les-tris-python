def tri_selection(l):
    for i in range(len(l)-1):#on parcourt la liste juqu'à l'avant dernier élément
        mini = i#on va chercher le plus petit élément à partir de i
        for j in range(i+1,len(l)):#on part du rang i et on cherche des elements inferieurs
            if l[j]<l[mini]:#on verifie si l'élément est plus petit que l(mini)
                mini = j#l'element j est plus petit que mini 
        l[i],l[mini] = l[mini],l[i]#on echange l'element i avec l'element mini
    return l


def tri_select_rec(l):
    if len(l)<=1:
        return l 
    mini = 1
    k=[]
    for i in range(1,len(l)):
        if l[i]<l[1]:
            mini = i 
    l[i],l[mini] = l[mini], l[i]#on echange l'element i avec l'element mini
    j=l[i]
    k.append(j)    
    tri_select_rec(l[1::])#on fait appel a la fonction avec une liste sans le rang minimum
    return k
