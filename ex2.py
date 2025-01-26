#Filtrar números pares de uma lista (com filter)
#Escreva uma função que, utilizando filter e uma função lambda, receba uma lista
#de números inteiros e retorne apenas os números pares.
#Exemplo de entrada: [1, 2, 3, 4, 5]
#Exemplo de saída: [2, 4]

def filtrar_par(num):
    return list(filter(lambda x: x % 2 == 0, num))

numeros = [1,2,3,4,5,6,7,8,9,10]
pares = filtrar_par(numeros)

print(f'Os números pares da lista são: {pares}')