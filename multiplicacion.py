num1 = 246810123
num2 = 135794656
def multiplicar_grande(a, b):
    if b == 0:
        return 0

    mitad = multiplicar_grande(a, b // 2)
    
    if b % 2 == 0:
        return mitad + mitad

    else:
        return a + mitad + mitad


resultado = multiplicar_grande(num1, num2)

print("Resultado:", resultado)