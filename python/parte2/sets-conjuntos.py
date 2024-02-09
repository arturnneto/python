"""
suportam apenas elementos unicos
nao tem indice
podem ser iterados
nao aceita valores duplicados <-- uso dele
"""

s1 = {1, 2, 3, 4, 5, 6}
print(s1)

s1.add(7)  # adiciona um valor
s1.discard(2)  # remove um valor
s1.update('Artur')  # itera sob os valores adicionados

print()

l1 = [1, 2, 3, 4, 5, 7, 1, 5, 8, 2, 0, 8, 9, 5, 3, 1, 6, 3, 7, 3, 1, 7, 1]
l1 = set(l1)
l1 = list(l1)
print(l1)

print()

s2 = {1, 2, 3, 4, 5}
s3 = {1, 2, 3, 4, 5, 6}
s4 = s1 | s2  # une todos os elementos presentes nos sets
      # & --> une os elementos presentes nos dois sets
      # ^ --> pega os valores exclusivos dos sets
      # - --> pega os valores exclusivos do set da esquerda
print(s4)

