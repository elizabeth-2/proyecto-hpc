import math
from concurrent.futures import ProcessPoolExecutor


def calcular(x):
    """
    Realiza la operación matemática sobre un dato.
    """
    return math.sqrt(x) + x**2 + math.sin(x) + math.cos(x) + math.log(x)


def procesar_paralelo(datos, workers):
    """
    Procesa los datos utilizando múltiples procesos.
    """
    with ProcessPoolExecutor(max_workers=workers) as executor:
        resultados = list(executor.map(calcular, datos))

    return resultados


if __name__ == "__main__":

    # Crear datos
    datos = range(1, 100001)

    # Procesar utilizando 2 workers
    resultados = procesar_paralelo(datos, 2)

    print("Cantidad de datos procesados:", len(resultados))
    print("Primer resultado:", resultados[0])
    print("Último resultado:", resultados[-1])