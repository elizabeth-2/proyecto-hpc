import math
import time


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

# Medir tiempo de procesamiento secuencial
inicio = time.perf_counter()

resultados = procesar_secuencial(datos)

fin = time.perf_counter()

tiempo = fin - inicio

print("Cantidad de datos procesados:", len(resultados))
print("Primer resultado:", resultados[0])
print("Último resultado:", resultados[-1])
print("Tiempo de ejecución:", tiempo, "segundos")