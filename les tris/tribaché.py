def uni(k, n):
    str_num = str(k)
    list=[int(chiffre) for chiffre in str_num]
    return list[n]

def concatenation(tab):
    dictionnaire=[]
    for i in range(10,0,-1):
        for j in tab:
            if j[1]==i:
                dictionnaire.append(j[1])
                print(dictionnaire)
    return dictionnaire


#on veut creer une nouvelle liste mais qui contient des tuples, et non pas un dictionnaire 
def remplissage_tuple_de_liste(tab, compteur):
    l=[]
    for i in tab:
        try:
            k=(i, uni(i,compteur))
            l.append(k)
        except IndexError:
            continue
    return l        


def rang_max(tab): ## le nombre maximal d'iterations 
    rang=0
    for i in tab:
        if rang<= len(str(i)):
            rang= len(str(i))
    return rang

def tri_baché(tab):
    rang_m = rang_max(tab)
    n=0
    nl=[]
    l = remplissage_tuple_de_liste(tab,n)
    for i in range(rang_m, 0, -1):
        print(nl)
        l=remplissage_tuple_de_liste(nl,i)
        nl=concatenation(l)
        n+=1
    return nl
l=[44545,22,248,1222,33,1,7,2,9]
p=remplissage_tuple_de_liste(l,0)
print(p)
print(concatenation(p))