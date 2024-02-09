def fala_oi():
    return f'Oi Artur'


def saudar(nome, saudacao):
    return f'{saudacao} {nome}'


def mestre(nome, saudacao):
    return fala_oi(), saudar(nome, saudacao)


var = mestre('artur', 'ola')
print(var)

print()


def mestra(funcao):
    return funcao()


var2 = mestra(fala_oi)
print(var2)

