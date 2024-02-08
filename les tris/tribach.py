def rang_max(tab): ## le nombre maximal d'iterations 
    rang=0
    for i in tab:
        if rang<= len(str(i)):
            rang= len(str(i))
    return rang

#def remplissage_rang(dic, rang):#rempli une liste avec le chiffre de chaque rang, mais il faut faire ca sur un deuxieme dictionnaire
    l=[]
    for key in dic:
        k=dic[key]
        p=k[rang]
        l.append(p)
    return l 
#def comparaison(tab):
    dico = dico(tab)
    rang_maxi = rang_max(tab)
    rang=0
    while rang<= rang_maxi:
        liste = remplissage_rang(dico, rang)
        tri_insertion(liste)
        

#def comparaison_dico(dictio):
    l=[dictio[key] for key in dictio ]
    
    return l
def uni(k,n):##fn qui extrait l'unité et le rang 
    str_num = str(k)
    list=[int(chiffre) for chiffre in str_num]
    return list[n]

def dico(tab):##cree un dictionnaire avec la liste d'unité 
    di={}
    for j in range(5):
        for i in tab:
            di[i]=uni(i,j)
        print(di)
    print(rang_max)



def tri_insertion(l):
    for i in range(1,len(l)):
        j=i
        while j>0 and l[j-1]>l[j]:
            l[j],l[j-1]=l[j-1],l[j]
            j-=1
    return l    
l=[33,57,2444,32335,223]
print(dico(l))




        
        

    