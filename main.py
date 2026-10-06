import math


def calcular(x):
    return math.sqrt(x) + x**2 + math.sin(x) + math.cos(x) + math.log(x)


# Crear datos
datos = range(1, 100001)

# Procesar los datos
resultados = []

for x in datos:
    resultados.append(calcular(x))

print("Cantidad de datos procesados:", len(resultados))
print("Primer resultado:", resultados[0])
print("Último resultado:", resultados[-1])