"""
ejercicio 1 recursividad 4
"""
def mayor_lista(lista):
    if len(lista) == 1:
        return lista[0]

    mayor_resto = mayor_lista(lista[1:])

    if lista[0] > mayor_resto:
        return lista[0]
    else:
        return mayor_resto

numeros = [3, 8, 2, 15, 7, 10]
print("El mayor valor es:", mayor_lista(numeros))
