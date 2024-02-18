def uni(k, n):#on veut le n-eme chiffre de k(centaines, dizaines, unités, etc...) a partir de la droite
    str_num = str(k)
    list=[int(chiffre) for chiffre in str_num]
    return list[-n] if n <= len(list) else 0

def concatenation(tab):#on veut concatener les liste en fonction du rang actuel
    bac = []#la liste rempli de sous listes dans lequelles on a mettra les elements en fonction de l'index de 0 a 9
    for p in range(10):
        bac.append([])
    for j in tab:#comme les elements de tab sont en tuples(pour ne pas perdre "l'adresse du nombre"), alors on ajoute l'element j[0] dans la l'index qui convient
        bac[j[1]].append(j[0])
    liste_n_eme = []
    for l_n_chiffre in bac:#on reconvertit notre liste de liste en une liste simple 
        for elt in l_n_chiffre:
            liste_n_eme.append(elt)
    return liste_n_eme

def remplissage_tuple_de_liste(tab, compteur):#convertir les elements de tab en tuples avec le deuxieme element qui correspond au rang dans lequel on tri
    l=[]
    for i in tab:
        k=(i, uni(i,compteur))
        l.append(k)
    return l        

def rang_max(tab):#nombre d'iteration maximal de la fonction tri_baché
    rang=0
    for i in tab:
        if rang<= len(str(i)):
            rang= len(str(i))
    return rang

def tri_baché(tab):
    rang_m = rang_max(tab)
    for i in range(1, rang_m + 1):#on commence par le rang 1 car uni utilisera le rang -1 puisque on commence a partir de la droite 
        tab = remplissage_tuple_de_liste(tab,i)
        tab = concatenation(tab)#on concatene pour chaque rang
    return tab

l=[44545,22,248,1222,33,1,7,2,9]
print(tri_baché(l))
