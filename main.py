import math


def calcular(x):
    """
    Realiza la operación matemática sobre un dato.
    """
    return math.sqrt(x) + x**2 + math.sin(x) + math.cos(x) + math.log(x)


def procesar_secuencial(datos):
    """
    Procesa todos los datos de manera secuencial.
    """
    resultados = []

    for x in datos:
        resultados.append(calcular(x))

    return resultados


# Crear datos
datos = range(1, 100001)

# Procesamiento secuencial
resultados = procesar_secuencial(datos)

print("Cantidad de datos procesados:", len(resultados))
print("Primer resultado:", resultados[0])
print("Último resultado:", resultados[-1])