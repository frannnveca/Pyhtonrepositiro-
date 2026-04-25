agenda = []
hora_actual = 0

actividades = [
    ("10.15 ", " 13.30", "clase"),
    ("20.00 ", " 21.15", "netflix"),
    ("15.45 ", " 17.00", "clase"),
    ("17.45 ", " 19.00", "tareas"),
    ("21.30 ", " 21.50", "cena"),
    ("8.00 ", " 9.15", "Desayuno"),
    ("14.00 ", " 15.30", "tareas"),
    ("13.45 ", " 14.15", "almuerzo"),
    ("9.30 ", " 10.00", "gym")
]
def convertir_minutos(hora):
    partes = hora.split(".")
    horas = int(partes[0])
    minutos = int(partes[1])
    return horas * 60 + minutos

n = len(actividades)
for i in range(n):
    for j in range(n - 1):
        if convertir_minutos(actividades[j][1]) > convertir_minutos(actividades[j + 1][1]):
            temp = actividades[j]
            actividades[j] = actividades[j + 1]
            actividades[j + 1] = temp

for inicio, fin, nombre in actividades:
    if convertir_minutos(inicio) >= hora_actual:
        agenda.append((inicio, fin, nombre))
        hora_actual = convertir_minutos(fin)


print("**Agenda ideal***")
for actividad in agenda:
    print(actividad[0]," - ", actividad[1], "-", actividad[2])
    