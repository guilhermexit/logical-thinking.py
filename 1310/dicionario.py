#Dicionário

computador = {'CPU':'Intel', 'RAM':'16GB', 'SSD':'1TB'}
print('=' * 30)

for chave in computador.keys():
    print(f'Chave: {chave} - Valor: {computador[chave]}')


print('=' * 30)

dicio_cores = {'amarelo':10, 'vermelho':2, 'cinza':55}


if 'amarelo' in dicio_cores:
    print(f"A cor está contida na chave {dicio_cores['amarelo']}")

print('=' * 30)

if 10 in dicio_cores.values():
    print("Valor encontrado!")

print('=' * 30)


#Uptade
python = {'aluno' : 'Xiteira'}

python['idade'] = 19

print(python, '\n =====================================' )

#Excluindo e retornando o item excluído

listaMercado = {'banana':10, 'maçã':2, 'pêra':55, 'Ovos':23}

ovosDel = listaMercado.pop('Ovos')


listaMercado.update({'Ovos': ovosDel})

print(listaMercado)

print('=' * 30)

