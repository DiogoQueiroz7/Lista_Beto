#Dicionário de números pares e ímpares
#Escreva uma função que receba uma lista de números inteiros e utilize lambda e
#filter para dividir a lista em números pares e ímpares. Retorne um dicionário com
#duas chaves: "pares" e "ímpares".
#Exemplo de entrada: [1, 2, 3, 4, 5, 6]
#Exemplo de saída: {"pares": [2, 4, 6], "ímpares": [1, 3, 5]}

def filtrar_impar_par(numeros):
    pares = list(filter(lambda x: x % 2 == 0, numeros))
    impares = list(filter(lambda x: x % 2 == 1, numeros))
    return {f'Pares':pares, 'Impares': impares}

numeros = [1,2,3,4,5,6,7,8,9,10]

resultado = filtrar_impar_par(numeros)

print(f'Os números pares e impares são: {resultado}')