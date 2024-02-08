
def tam(tab, noeud, n):
    k=noeud
    j=2*k
    while j<=n:
        if j<n and tab[j]<tab[j+1]:
            j+=1
        if tab[k]<tab[j]:
            tab[k],tab[j]=tab[j],tab[k]
            k=j
            j=2*k
        else:
            j=n+1
    

def tpt(tab):
    k=len(tab)
    for i in range(k//2, 1,-1):
        tam(tab,i,k)
    for i in range(k,2,-1):
        tab[i], tab[1]= tab[1], tab[i]
        tam(tab, 1,i-1)
    

l=[3,8,99,5555,885,32,34,11,52]
print(tpt(l))
            















def tripartas(t):
    for i in range (len(t)/2,1,-1):
        tamiser(t,)