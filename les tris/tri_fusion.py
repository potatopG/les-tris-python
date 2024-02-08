def fusion(left, right):#fusionne deux listes triées
    if not left:#si left est vide on
        return right
    if not right:#si right est vide on
        return left
    if left[0] < right[0]:#si le premier élément de left est plus petit que le premier élément de right
        return [left[0]] + fusion(left[1:], right)#on renvoie le premier élément de left et on fusionne le reste de left avec right
    return [right[0]] + fusion(left, right[1:])# sinon on renvoie le premier élément de right et on fusionne le reste de right avec left

def tri_fusion(l):#CE PROGRAMME EST JUSTE LE PROGRAMME QUI ORGANISE ET L4AUTRE QUI TRI ET FUSIONNE 
    if len(l) <= 1:
        return l
    else:#on coupe la liste en deux
        mid = len(l) // 2
        left = l[:mid]#on prend la partie gauche
        right = l[mid:]#on prend la partie droite
        return fusion(tri_fusion(left), tri_fusion(right))#on fusionne les deux parties triées


l = [3,5,7,4,2,6,1]
print(tri_fusion(l))