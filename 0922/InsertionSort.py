#Insertion Sort


def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i-1
        while j >= 0 and key < lista[j]:
            lista[j+1] = lista[j]
            j-=1
        lista[j+1] = key
    print(lista)


#Principal
lista = [12, 11, 13, 5, 6]
insertion_sort(lista)

