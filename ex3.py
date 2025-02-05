from functools import reduce

def somar_lista(lista):
    return reduce(lambda x,y: x+y, lista)

lista = [1,2,3,4,5,6,7,8,9,10]
resultado = somar_lista(lista)
print(f'O resultado é: {resultado}')