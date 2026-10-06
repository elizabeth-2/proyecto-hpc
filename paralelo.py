import math
import time
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

    datos = range(1, 100001)

    # Probar diferentes cantidades de workers
    for workers in [1, 2, 4]:

        inicio = time.perf_counter()

        resultados = procesar_paralelo(datos, workers)

        fin = time.perf_counter()

        tiempo = fin - inicio

        print("\nWorkers utilizados:", workers)
        print("Cantidad de datos procesados:", len(resultados))
        print("Primer resultado:", resultados[0])
        print("Último resultado:", resultados[-1])
        print("Tiempo de ejecución:", tiempo, "segundos")