#Escreva uma função que receba uma lista de números inteiros e utilize map e filter
#para criar um dicionário que agrupe os números em três categorias:
#o "positivos" (números maiores que 0)
#o "negativos" (números menores que 0)
#o "zeros" (números iguais a 0).
#o Exemplo de entrada: [1, -2, 0, 3, -5, 0]
#o Exemplo de saída: {"positivos": [1, 3], "negativos": [-2, -5], "zeros": [0, 0]}

def ordernas_num(lista):
    positivos = list(map(lambda x: x, filter(lambda x: x>0, lista)))
    negativos = list(map(lambda x: x, filter(lambda x: x<0, lista)))
    zeros = list(map(lambda x: x, filter(lambda x: x == 0, lista)))
    return {f'Positivos':positivos, 'Negativos':negativos, 'Zeros':zeros}

lista = [1,2,3,4,5,6,-7,-8,-9,-10,0,0]
resultado = (ordernas_num(lista))
print(f'Os numeros agrupados ficam: {resultado}')
    
    
    
    
    
    