nome = input("Qual seu nome?")

if nome:
    print(nome)
else:
    print("Você não digitou nada.")

print()  # como simplificar:

print(nome or 'Você não digitou nada.')

print() ###################

a = False
b = None
c = 0
d = {}
e = []
f = "Amorim"
g = 22
variavel = a or b or c or d or e or f or g
print(variavel)
