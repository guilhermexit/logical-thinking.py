#Bubble Sort

def troca(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]


#Programa principal
lista = [40, 30, 20, 50, 10]
cont = 0
print(lista)
for item in range(len(lista)):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i+1]:
            troca(lista, i, i+1)
        cont += 1
print(lista)
