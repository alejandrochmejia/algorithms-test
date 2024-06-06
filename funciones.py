#Alejandro Chávez (32.278.392)
#José Santana()

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
def comparar_sublistas(sublista1, sublista2):
    if sublista1[0] != sublista2[0]:
        return sublista1[0] - sublista2[0]
    elif sublista1[1] != sublista2[1]:
        return sublista1[1] - sublista2[1]
    else:
        return sublista1[2] - sublista2[2]

def mergelistas(left, right):
    result = []
    while left and right:
        if comparar_sublistas(left[0], right[0]) < 0:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left if left else right)
    return result

def mergesortlistas(lista):
    if len(lista) <= 1:
        return lista
    mid = len(lista) // 2
    left = lista[:mid]
    right = lista[mid:]
    return mergelistas(mergesortlistas(left), mergesortlistas(right))

#Operacion C

#Operacion D

#Operacion E

#Operacion F