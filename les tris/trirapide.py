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

