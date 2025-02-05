from functools import reduce

def calcular_media(alunos):
    resultado = {}
    for nome, notas in alunos.items():
        peso = notas[-1]
        media = reduce(lambda x, nota: x + nota * peso, notas[:-1], 0)
        ponderada = media / ((len(notas) -1) *peso)
        
        resultado[nome] = ponderada
        
    return resultado
    
alunos = {
    "João": [8, 7, 9, 2],
    "Ana": [5, 6, 7, 3]
}

print(calcular_media(alunos))



