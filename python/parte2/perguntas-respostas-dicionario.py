perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {
            'a': 2,
            'b': 3,
            'c': 4,
            'd': 5
        },
        'resposta_certa': 'c'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 5 + 2?',
        'respostas': {
            'a': 5,
            'b': 6,
            'c': 7,
            'd': 8
        },
        'resposta_certa': 'c'
    }
}

respostas_certas = 0
for cp, cr in perguntas.items():
    print(f'{cp}: {cr["pergunta"]}')

    print(f'Escolha uma das opções abaixo: ')

    for rk, rv in cr['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Insira sua resposta:')

    if resposta_usuario == cr['resposta_certa']:
        print('Você acertou!')
        respostas_certas += 1
    else:
        print('Resposta incorreta!')

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100
print(f'Você acertou {porcentagem_acerto}% das perguntas.')
