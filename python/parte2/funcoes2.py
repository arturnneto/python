def funcao(var):
    return var
    print('isso nao será executado')  # pois fica abaixo do return


variavel = funcao('valor que eu quero')

if variavel:
    print(variavel)
else:
    print('nenhum valor.')

print()  #############################


def divisao(n1, n2):
    if n2 > 0:
        return n1 / n2


divide = divisao(15, 5)

if divide:
    print(divide)
else:
    print('conta invalida')
