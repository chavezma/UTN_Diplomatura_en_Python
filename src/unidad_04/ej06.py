"""
Cree una función que tome la siguiente lista y reordene de menor a mayor sus componentes:
[3, 44, 21, 78, 5, 56, 9]
"""

lista = [3, 44, 21, 78, 5, 56, 9, 7]

def swap(la_lista, i, j):
    temp = lista[j]
    lista[j] = lista[i]
    lista[i] = temp

def ordena_lista_iterativo(ls):
    la_lista = ls
    for x in range(0, len(ls)):
        for y in range(0, len(ls)):
            if x < y and ls[x] > ls[y]:
                swap(ls, x, y)

    return la_lista

def ordena_lista_recursivo(ls):
    if len(ls) == 2:
        return sorted(ls)

    if len(ls) == 1:
        return ls

    pivot = int(len(ls) / 2)

    return merge(ordena_lista_recursivo(ls[0:pivot]), ordena_lista_recursivo(ls[pivot:]))

def merge(l1, l2):
    nueva_lista = []

    while len(l1) > 0 and len(l2) > 0:
        while l1 and l2:
            if l1[0] < l2[0]:
                nueva_lista.append(l1[0])
                del l1[0]
            else:
                nueva_lista.append(l2[0])
                del l2[0]

    if len(l1) > 0:
        while l1:
            nueva_lista.append(l1[0])
            del l1[0]
    else:
        while l2:
            nueva_lista.append(l2[0])
            del l2[0]

    return nueva_lista

# merge([3, 4], [1, 2])

print("--------------------------------------------")
print("resultado iterativo => ", ordena_lista_iterativo(lista))
print("resultado recursivo => ", ordena_lista_recursivo(lista))
