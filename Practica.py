def calcular_promedio(lista_numeros):
    '''calcula el promedio de una lista de números.

    Argumentos:
    lista_numeros (list): Una lista que contiene números enteros o decimales.

    Retorna:
    float: El resultado del promedio. Devuelve 0.0 si la lista no tiene elementos.'''
    
    if not lista_numeros:
        return 0.0

    return sum(lista_numeros) / len(lista_numeros)