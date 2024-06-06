from functools import cmp_to_key
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
def shellsortalfabetico(lista):
    n = len(lista)
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = lista[i]
            j = i
            while j >= intervalo and lista[j - intervalo] > temp:
                lista[j] = lista[j - intervalo]
                j -= intervalo
            lista[j] = temp
        intervalo //= 2
    return lista

#Operacion D
def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    mid = len(lista) // 2
    left_half = lista[:mid]
    right_half = lista[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged
#Operacion E

#Operacion F
def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end=" ")
    for j in hashTable[i]:
        print("-->", end=" ")
        print(j, end=" ")
    print()

def Hashing(keyvalue,HashTable):
    return keyvalue % len(HashTable)

def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue,Hashtable)
    Hashtable[hash_key].append(value)