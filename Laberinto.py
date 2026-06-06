def imprime(mat):
    for fil in mat:
        print(fil)
    print()

def valido(lab, res, f, c):

    if f < 0 or f >= len(lab):
        return False

    if c < 0 or c >= len(lab[0]):
        return False

    if lab[f][c] == 0:
        return False

    if res[f][c] == 1:   
        return False

    return True

def sollab(lab, res, f, c):

    if f == 2 and c == 0:
        res[f][c] = 1
        imprime(res)
        return True

    if valido(lab, res, f, c):

        res[f][c] = 1
        imprime(res)
        if sollab(lab, res, f, c + 1):
            return True
        if sollab(lab, res, f + 1, c):
            return True
        if sollab(lab, res, f, c - 1):
            return True
        if sollab(lab, res, f - 1, c):
            return True

        res[f][c] = 0
        return False

    return False

lab = [
    [1,1,1,1,0,1,1,1,1],
    [1,0,0,1,0,1,0,0,0],
    [1,1,0,1,1,1,1,0,1],
    [0,1,0,1,0,0,1,0,1],
    [1,1,1,1,1,1,1,1,1],
    [1,0,1,0,0,0,1,0,1],
    [1,1,1,1,0,1,1,0,1],
    [1,0,0,1,0,1,0,0,1],
    [1,1,1,1,0,1,1,1,1]
]

res = [[0 for _ in range(len(lab[0]))]
       for _ in range(len(lab))]

if sollab(lab, res, 0, 0):
    print("Salio del lab")
else:
    print("No hay salida")