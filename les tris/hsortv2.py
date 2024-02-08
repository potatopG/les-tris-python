def heapify(tab, n, i):
    smol = i
    left_child=2*i+1
    right_child=2*i+2
    
    if left_child < n and tab[left_child]<tab[smol]:
        smol = left_child
    
    if right_child < n and tab[right_child]<tab[smol]:
        smol = right_child
        
    if smol != i:
        tab[i], tab[smol] = tab[smol] , tab [i]
        heapify(tab, n, smol)

def build_min_heap(tab):
    n=len(tab)
    for i in range(n//2-1, -1, -1):
        heapify(tab,i,0)


def heap_sort(tab):
    n = len(tab)
    build_min_heap(tab)
    for i in range(n-1, 0, -1):
        tab[i], tab[0] = tab[0], tab[i]
        heapify(tab, i , 0)
        
