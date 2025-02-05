def ordernas_num(lista):
    positivos = list(map(lambda x: x, filter(lambda x: x>0, lista)))
    negativos = list(map(lambda x: x, filter(lambda x: x<0, lista)))
    zeros = list(map(lambda x: x, filter(lambda x: x == 0, lista)))
    return {f'Positivos':positivos, 'Negativos':negativos, 'Zeros':zeros}

lista = [1, -2, 0, 3, -5, 0]
resultado = (ordernas_num(lista))
print(f'Os numeros agrupados ficam: {resultado}')
