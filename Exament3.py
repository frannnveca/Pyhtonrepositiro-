def mostrar(mat):

    for f in mat:

        for c in f:
            print(str(c).rjust(3), end=" ")

        print()

    print()


lab = [

    [1, 1, 1, 1, 0, 1, 1, 1, 1],

    [-2, 0, 0, -1, 0, 1, 0, 1, 0],

    [1, 1, 0, 1, 1, 1, 0, 1, 0],

    [0, 1, 0, -1, 0, 0, 0, -1, 0],

    [1, 1, 1, 1, 1, 1, 1, 1, 0],

    [-1, 0, 0, 0, 0, 0, 0, 1, 1],

    [1, 1, 1, 1, -1, 1, 1, 1, 0],

    [1, 0, 0, 1, 0, 1, 0, 1, 0],

    [1, 1, -1, 1, 1, 1, 0, 1, 1]

]

fin = (0, 0)

vida = 3

cam = []

vis = set()


def valido(x, y):

    if x < 0 or x > 8 or y < 0 or y > 8:
        return False

    if lab[x][y] == 0:
        return False

    if (x, y) in vis:
        return False

    return True


def bt(x, y, v):

    if (x, y) == fin:

        cam.append((x, y))

        return True

    if valido(x, y):

        nv = v

        if lab[x][y] < 0:
            nv += lab[x][y]

        if nv > 0:

            vis.add((x, y))

            cam.append((x, y))

            if bt(x + 1, y, nv):
                return True

            if bt(x, y + 1, nv):
                return True

            if bt(x - 1, y, nv):
                return True

            if bt(x, y - 1, nv):
                return True

            cam.pop()

            vis.remove((x, y))

    return False


print("\n'LABERINTO ORIGINAL'\n")

mostrar(lab)

if bt(8, 0, vida):

    print("\n'SI SE ENCONTRO CAMINO'")

    sol = []

    for i in range(9):

        fila = []

        for j in range(9):

            if (i, j) in cam:
                fila.append("*")
            else:
                fila.append(lab[i][j])

        sol.append(fila)

    mostrar(sol)

    print("\nRECORRIDO:")

    for p in cam:
        print(p)

else:

    print("x 'NO HAY CAMINO' x")