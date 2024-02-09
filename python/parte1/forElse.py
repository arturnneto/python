variavel = ["Artur", "Jorge", "Amorim", "Neto"]

for valor in variavel:
    if valor.lower().startswith("a"):
        continue
    print(valor)
else:
    print("Não existe palavra com A.")

