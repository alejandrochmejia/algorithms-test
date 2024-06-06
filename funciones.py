#Operacion A
def quicksort_descendente(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[-1]
        menores = [x for x in lista[:-1] if x >= pivote]
        mayores = [x for x in lista[:-1] if x < pivote]
        return quicksort_descendente(mayores) + [pivote] + quicksort_descendente(menores)
    
#Operacion B

#Operacion C

#Operacion D

#Operacion E

#Operacion F