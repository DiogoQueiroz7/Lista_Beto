def filtrar_par(num):
    return list(filter(lambda x: x % 2 == 0, num))

numeros = [1,2,3,4,5,6,7,8,9,10]
pares = filtrar_par(numeros)

print(f'Os números pares da lista são: {pares}')