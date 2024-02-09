string = "Meu nome é Artur Jorge"
lista = string.split(' ')  # divide a string pelo caractere especificado
string2 = ', '.join(lista)  # junta a lista com o caractere especificado

print(string)
print(lista)
print(string2)

print()  ##################

for indice, valor in enumerate(lista):  # enumera a lista por indices
    print(indice, valor,)

print()  #############

lista = ['teste', 'testando', 'testar', 1, 2, 3, 4, 5, 6]
n1, n2, n3, *resto, ultimo_da_lista = lista     # atribui o valor da variavel de acordo com o índice da lista
print(n1, n2, resto, ultimo_da_lista)           # o "*resto" transforma os valores restantes em outra lista
