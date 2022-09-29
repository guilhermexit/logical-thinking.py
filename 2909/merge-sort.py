def merg_sort(lista):
    if len(lista) > 1:

        #Encontrando o meio da lista
        meio = len(lista) // 2

        #Dividindo a lista em duas Right e Left
        left = lista[:meio]
        right = lista[meio:]

        #Ordenando a primeira lista
        merg_sort(left)

        #Ordenando a segunda lista
        merg_sort(right)
       
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                lista[j] = left[i]
                i+=1
            else:
                lista[k] = right[j]
                j+=1
            k+=1

        #Verificando os elementos da lista Left
        while i < len(left):
            lista[k] = left[i]
            i+=1
            k+=1

        #Verificando os elementos lista Right
        while j < len(right):
            lista[k] = right[j]
            j+=1
            k+=1

#Principal
lista = [12, 11, 13, 5, 6, 7]
print(f'Lista: {lista}')
merg_sort(lista)
print(f'Lista Ordenada: {lista}')

