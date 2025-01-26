# Elevar números ao quadrado e ordenar (com map e sorted)
#Crie uma função que eleve ao quadrado todos os números de uma lista, utilizando
#map, e depois retorne a lista ordenada.
#Exemplo de entrada: [3, 1, 4, 2]
#Exemplo de saída: [1, 4, 9, 16]

def ordernar_num(numeros):
    return list(sorted(map(lambda x: x**2, numeros)))

numeros = [3, 1, 4, 2]
ordenados = ordernar_num(numeros)

print(f'Os números ao quadrado ordenados são: {ordenados}')