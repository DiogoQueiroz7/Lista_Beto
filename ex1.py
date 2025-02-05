def dobrar_num(numeros):
    return list(map(lambda x:x*2, numeros))

numeros = [1,2,3,4,5,6,7,8,9,10]
dobro = dobrar_num(numeros)
print(f'Os números dobrados são: {dobro}')