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
    izquierda_lista = lista[:mid]
    derecha_lista = lista[mid:]

    return merge(merge_sort(izquierda_lista), merge_sort(derecha_lista))


def merge(left, right):
    result = []
    izquierda_elementos = 0
    derecha_elementos = 0

    while izquierda_elementos < len(left) and derecha_elementos < len(right):
        if left[izquierda_elementos] <= right[derecha_elementos]:
            result.append(left[izquierda_elementos])
            izquierda_elementos += 1
        else:
            result.append(right[derecha_elementos])
            derecha_elementos += 1

    result.extend(left[izquierda_elementos:])
    result.extend(right[derecha_elementos:])

    return result
#Operacion E
def heapsort(arr):
    def heapify(arr, n, i):
        Masgrande = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            Masgrande = l

        if r < n and arr[Masgrande] < arr[r]:
            Masgrande = r

        if Masgrande != i:
            arr[i], arr[Masgrande] = arr[Masgrande], arr[i]
            heapify(arr, n, Masgrande)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr
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