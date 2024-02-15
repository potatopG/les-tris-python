# les-tris-pour-robbena-
# tri a bulle:
def tri_abulle(l):
    verif=True
    while verif:
        verif=False
        for k in range(1,len(l)):
            if l[k]<l[k-1]:
                l[k], l[k - 1] = l[k - 1], l[k]
                verif =False
    return l

l=tri_abulle([44,75,59])
print(l)

#tri par insertion
def tri_inser(l):
    for k in range(1,len(l)):
        cle=l[k]
        i=k
        while i>=1 and cle<l[i-1]:
            l[i]=l[i-1]
            i-=1
        l[i]=cle
    return l
l=tri_inser([44,75,59])
print(l)
#tri par insertion (recurssivite)
def tri_insertion(t,j=1):
    if j<len(t):
        insere(t,j)
        tri_insertion(t,j+1)
    return t
    
def insere(t,j):
    if j>0 and t[j]<t[j-1]:
        t[j-1],t[j]=t[j],t[j-1]
        insere(t,j-1)
l=tri_insertion([44,75,59])
print(l)
#tri rapide
def partiton(t,d,f):
    pivot=t[f-1]
    k=d
    for i in range (d,f-1):
        if t[i]<pivot:
            t[i],t[k]=t[k],t[i]
            k+=1
        t[f-1],t[k]=t[k],t[f-1]
    return k
def tri_rapide(t, d, f):
    if d < f:
        pivot =partition(t, d, f)
        tri_rapide(t, d, pivot)
        tri_rapide(t, pivot + 1, f)
    return t
