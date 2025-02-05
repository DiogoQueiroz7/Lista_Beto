def filtrar_nomes(nomes):
    return list(filter(lambda x: len(x) >= 5, nomes))

nomes = ["Ana", "Lucas", "Fernanda", "João"]

nomes_maiores = filtrar_nomes(nomes)

print(f'Os nomes com mais de 5 letras são: {nomes_maiores}')