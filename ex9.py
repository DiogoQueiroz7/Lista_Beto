def filtrar_num(lista):
    def media_tuple(x):
        return sum(x) / len(x)

    medias = list(map(media_tuple, lista))

    resultado = list(filter(lambda x: media_tuple(x) >= 5, lista))

    return resultado

lista_num = [(2, 8), (4, 5, 6), (1, 2)]

print(filtrar_num(lista_num))
