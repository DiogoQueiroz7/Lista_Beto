#Escreva uma função que receba uma lista de tuplas, onde cada tupla contém
#números inteiros. Utilize map e filter para filtrar as tuplas cuja média dos valores
#seja maior que 5.
#Exemplo de entrada: [(2, 8), (4, 5, 6), (1, 2)]
#Exemplo de saída: [(2, 8), (4, 5, 6)]

def filtrar(num):
    return tuple(map(lambda x: x+x/x, filter(lambda x: x>5, num)))

num = [(1,2,3,4,5), (2,3), (4,6,7)]
result = filtrar(num)

print(result)