"""
ejercicio 2 recursividad 5
multiplo de 5
"""
numeros = [5, 8, 10, 13, 20, 7,25,3,70,6]
def suma_multiplos_5(lista):
    if len(lista) == 0:
        return 0


    if lista[0] % 5 == 0:
        return lista[0] + suma_multiplos_5(lista[1:])
    else:
        return suma_multiplos_5(lista[1:])

print("La suma es:", suma_multiplos_5(numeros))