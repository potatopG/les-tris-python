from random import randint

def tri_rapide(l):
    if len(l)<=1:
        return l
    else:
        pipi,caca=[],[]
        pivot =l[-1]
        for i in range(len(l)-1):
            if l[i]<l[-1]:
                pipi.append(l[i])
            else:
                caca.append(l[i])
        return tri_rapide(pipi)+[l[-1]]+tri_rapide(caca)

l=[5,7,6,9,22,4,1,333]
print(tri_rapide(l))