
try:
    a = 1/0
    b = []
except NameError as erro:
    print(f'O erro foi de {erro}')
except (IndexError, KeyError) as erro:
    print(f'O erro foi de {erro}')
except Exception as erro:
    print(f'O erro foi de {erro}')
else:
    print('Código executado com sucesso.')
    print(b)
finally:
    a = None

print(a)
print('Vamos continuar.')
