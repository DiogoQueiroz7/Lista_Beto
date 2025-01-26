#Dobrar elementos de uma lista (com map)
#Escreva uma função que, utilizando map e uma função lambda, receba uma lista
#de números inteiros e retorne uma nova lista com todos os elementos dobrados.
#Exemplo de entrada: [1, 2, Exemplo de saída: [2, 4, 6, 8]
def dobrar_num(numeros):
    return list(map(lambda x:x*2, numeros))

numeros = [1,2,3,4,5,6,7,8,9,10]
dobro = dobrar_num(numeros)
print(f'Os números dobrados são: {dobro}')