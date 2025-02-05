from functools import reduce

def contar_letras(palavras):
    return reduce(lambda x,y: x+y, map(lambda x: len(x), palavras))
    
palavras = ['casa', 'python', 'lambda']
resultado = contar_letras(palavras)

print(resultado)