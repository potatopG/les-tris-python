def uni(k, n):
    str_num = str(k)
    list=[int(chiffre) for chiffre in str_num]
    return list[n]

def remplissage_tuple_de_liste(tab, compteur):
    l=[]
    for i in tab:
        try:
            k=(i, uni(i,compteur))
            l.append(k)
        except IndexError:
            continue
    return l   

def concatenation(tab):
    dictionnaire=[]
    l2=[]
    for i in range(10,0,-1):
        for j in tab:
            try:
                if j[1][i]==i:
                    dictionnaire.append(j[1])
                    print(dictionnaire)
            except: ValueError  
    return dictionnaire

def rang_max(tab): ## le nombre maximal d'iterations 
    rang=0
    for i in tab:
        if rang<= len(str(i)):
            rang= len(str(i))
    return rang

l=[253,66,33,21,45,76,23,2]

def tri_baché(tab):
    rang_m = rang_max(tab)
    n=0
    nl=[]
    l = []
    for i in range(rang_m, 0, -1):
        l=remplissage_tuple_de_liste(tab,i)
        print(l)
        nl=concatenation(l)
        print(nl)
    
    return nl
        
print(tri_baché(l))