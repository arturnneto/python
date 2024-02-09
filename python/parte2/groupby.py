from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Jorge', 'nota': 'A'},
    {'nome': 'Artur', 'nota': 'C'},
    {'nome': 'João', 'nota': 'D'},
    {'nome': 'Maria', 'nota': 'B'},
    {'nome': 'Felipe', 'nota': 'A'},
    {'nome': 'Vit', 'nota': 'F'},
    {'nome': 'Louisi', 'nota': 'B'},
    {'nome': 'Junior', 'nota': 'A'},
]
alunos.sort(key=lambda item: item['nota'])
alunos_agrupados = groupby(alunos, lambda item: item['nota'])

for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamento}')
    for aluno in valores_agrupados:
        print(aluno)
