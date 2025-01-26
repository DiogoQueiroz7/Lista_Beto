#Escreva uma função que receba uma lista de nomes e, utilizando filter, retorne
#apenas os nomes com mais de 5 letras.
#Exemplo de entrada: ["Ana", "Lucas", "Fernanda", "João"]
#Exemplo de saída: ["Lucas", "Fernanda"]

def filtrar_nomes(nomes):
    return list(filter(lambda x: len(x) > 5, nomes))

nomes = ["Ana", "Lucas", "Fernanda", "João", "Cristiano", "Diogo", "Julia", "Bruna", "Vanuza"]

nomes_maiores = filtrar_nomes(nomes)

print(f'Os nomes com mais de 5 letras são: {nomes_maiores}')