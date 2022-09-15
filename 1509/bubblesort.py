def troca(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]

def empurra(lista, n):
    for i in range(n-1):
        if lista[i] > lista[i+1]:
            troca(lista, i, i+1)

def bubble_sort(s):
    t = len(s)
    while t > 1:
        empurra(s, t)
        t -= 1
    



#PRINCIPAL
lista = [40, 30, 20, 50, 10]
bubble_sort(lista)
print(lista)