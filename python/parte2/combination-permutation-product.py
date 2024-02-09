from itertools import combinations, permutations, product

pessoas = ['Artur', 'Jorge', 'Amorim', 'Neto']
for grupo in combinations(pessoas, 2):
    print(grupo)

print()

for grupo in permutations(pessoas, 2):
    print(grupo)

print()

for grupo in product(pessoas, repeat=2):
    print(grupo)
