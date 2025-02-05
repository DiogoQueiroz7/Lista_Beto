def ordernar_num(numeros):
    return list(sorted(map(lambda x: x**2, numeros)))

numeros = [3, 1, 4, 2]
ordenados = ordernar_num(numeros)

print(f'Os números ao quadrado ordenados são: {ordenados}')