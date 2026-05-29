import random

print("---------------------------------------------")
n = int(input(" Ingresa el numero N: "))

"""
Funcion Matriz
"""
def crear_matriz(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            numero = random.randint(99, 999)
            fila.append(numero)
        matriz.append(fila)
    return matriz

"""
Funcion Mostrar Matriz
"""
def mostrar_matriz(matriz):
    print("\nMATRIZ:\n")
    for fila in matriz:
        for numero in fila:
            print(numero, end=" ")
        print()

"""
Divide y Venceras
"""
def contar_multiplos(matriz, inicio, fin):
    if inicio == fin:
        contador = 0
        for numero in matriz[inicio]:
            if numero % 5 == 0 or numero % 7 == 0:
                contador = contador + 1
        return contador
    medio = (inicio + fin) // 2
    izquierda = contar_multiplos(matriz, inicio, medio)
    derecha = contar_multiplos(matriz, medio + 1, fin)
    return izquierda + derecha


matriz = crear_matriz(n)
mostrar_matriz(matriz)
resultado = contar_multiplos(matriz, 0, n - 1)
print("\nCantidad de multiplos de 5 o 7:", resultado)
print("---------------------------------------------")