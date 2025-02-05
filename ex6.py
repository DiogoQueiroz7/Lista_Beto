def filtrar_impar_par(numeros):
    pares = list(filter(lambda x: x % 2 == 0, numeros))
    impares = list(filter(lambda x: x % 2 != 0, numeros))
    return {f'Pares':pares, 'Impares': impares}

numeros = [1,2,3,4,5,6,7,8,9,10]

resultado = filtrar_impar_par(numeros)

print(f'Os números pares e impares são: {resultado}')