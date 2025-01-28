from functools import reduce
#Crie uma função que, utilizando reduce e uma função lambda, receba uma lista de
#números inteiros e retorne a soma total dos números.
#Exemplo de entrada: [1, 2, 3, 4]
#Exemplo de saída: 10

def somar_lista(lista):
    return reduce(lambda x,y: x+y, lista)

lista = [1,2,3,4,5,6,7,8,9,10]
resultado = somar_lista(lista)
print(f'O resultado é: {resultado}')