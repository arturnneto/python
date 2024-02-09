def funcao(x='oi', y='Artur'):
    y = y.replace('neto', 'amorim')
    x = x.replace('tchau', 'ate logo')
    print(x, y)


funcao('oi', 'Artur')
funcao()
funcao(y='Artur', x='oI')
funcao('tchau', 'neto')
