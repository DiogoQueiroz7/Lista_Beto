from functools import reduce
#Crie uma função que receba uma lista de palavras e retorne a soma total de letras
#em todas as palavras, utilizando map para contar as letras e reduce para somar.
#Exemplo de entrada: ["casa", "python", "lambda"]
#Exemplo de saída: 16

def contar_letras(palavras):
    return reduce(lambda x,y: x+y, map(lambda x: len(x), palavras))
    
palavras = ['Diogo', 'Bruna', 'Cristiano']
resultado = contar_letras(palavras)

print(resultado)