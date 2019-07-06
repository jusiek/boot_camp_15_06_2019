lista = [5, 34, 56, 53,32, 57, 44, 4, 8]

i_max = 0
i_min = 0

for i in range (len(lista)):
    if lista [i] < lista [i_min]:
        i_min = i
    if lista [i] > lista [i_max]:
        i_min = i
temp = lista[i_max]
lista[i_max] = lista[i_min]
lista[i_min] = temp
