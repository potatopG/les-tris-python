def tri_insertion(l):
    for i in range(1,len(l)):
        j=i
        while j>0 and l[j-1]>l[j]:
            l[j],l[j-1]=l[j-1],l[j]
            j-=1
    return l
