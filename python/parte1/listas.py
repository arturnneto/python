lista = ['teste', True, 99]
print(lista[1])
lista[1] = False  # como troca valores dentro da lista
print(lista[1])

print()  ####################

print(lista[:1])  # exibe os valores da lista até o indice especificado

print()  ####################

lista2 = lista[::-1]  # adiciona os valores da lista para outra lista de tras pra frente por causa do -1
print(lista2)

print()  ####################

print(lista + lista2)
lista.extend(lista2)  # adiciona uma lista na outra
lista.append("adicionando")  # adiciona um valor no final da lista
lista.insert(0, 'insert')  # insere um valor na lista no indice especificado
lista.pop(1)  # tira um valor da lista
print(lista)

print()  ####################

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l1)
del(l1[3:5])  # deleta um intervalo de valores especificado pelo indice
print(l1)

print()  ########################

l2 = list(range(0, 100, 10))  # cria uma lista nova, do 0 ao 100, pulando de 10 em 10
print(l2)
