"""
Hacer una funcion recursiva que devuelva el promedio

de una lista de numeros

[2,4,6,4] -> 16/4 = 4
"""

numeros = [10,15,4,6,25]

def suma_recursiva(lista):
    # Caso base
    if len(lista) == 1:
        return lista[0]
    
    return lista[0] + suma_recursiva(lista[1:])

def promedio(lista):
    return suma_recursiva(lista) / len(lista)

print("Promedio:", promedio(numeros))