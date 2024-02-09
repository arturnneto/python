d1 = {'chave1': 'valor da chave'}
print(d1)

print()

d1['nova chave'] = 'valor da nova chave'
print(d1['chave1'])

print()

d2 = dict(chave1='valor da chave', chave2='valor da outra chave')
print(d2)

print()

d3 = {
    'str': 'valor',
    123: 'outro valor',
    (1, 2, 3, 4): 'mais um valor'
}

print(d3[1, 2, 3, 4])  # printa valores especificos do dicionario
print(d1.get('nome_da_chave'))  # pega um valor no dicionario
d1.update({'Nova_chave': 'novo_valor'})  # atualiza um valor no dicionario
d1['nome_da_chave'] = 'valor_da_chave'   # porem o jeito mais usado é esse
del d3['str']  # deleta um valor

for v in d3.values():
    print(v)

print()

for k, v in d3.items():  # iteraçao dos valores no dicionario
    print(k, ':', v)

print()

clientes = {
    'cliente1': {
        'nome': 'Artur',
        'idade': 20,
        'pais': 'Brasil'
    },
    'cliente2': {
        'nome': 'Jorge',
        'idade': 21,
        'pais': 'Brasil'
    }
}

for clientes_k, clientes_v in clientes.items():
    print(f'exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')
