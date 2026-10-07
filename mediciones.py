import time
import matplotlib


matplotlib.use("Agg")


import matplotlib.pyplot as plt


from paralelo import procesar_paralelo
from main import procesar_secuencial




# Cantidad de datos
datos = range(1, 100001)


# Cantidad de pruebas
PRUEBAS = 3


# Workers que se van a evaluar
workers_lista = [1, 2, 4]




def medir_secuencial():
    tiempos = []


    for i in range(PRUEBAS):
        inicio = time.perf_counter()


        procesar_secuencial(datos)


        fin = time.perf_counter()


        tiempos.append(fin - inicio)


    return tiempos




def medir_paralelo(workers):
    tiempos = []


    for i in range(PRUEBAS):
        inicio = time.perf_counter()


        procesar_paralelo(datos, workers)


        fin = time.perf_counter()


        tiempos.append(fin - inicio)


    return tiempos




def main():


    # -----------------------------
    # MEDICIÓN SECUENCIAL
    # -----------------------------


    print("===== PROCESAMIENTO SECUENCIAL =====")


    tiempos_secuencial = medir_secuencial()


    for i, tiempo in enumerate(tiempos_secuencial, 1):
        print(f"Prueba {i}: {tiempo:.6f} segundos")


    promedio_secuencial = sum(tiempos_secuencial) / PRUEBAS


    print(f"Promedio secuencial: {promedio_secuencial:.6f} segundos")




    # -----------------------------
    # MEDICIÓN PARALELA
    # -----------------------------


    print("\n===== PROCESAMIENTO PARALELO =====")


    promedios = {}


    for workers in workers_lista:


        tiempos = medir_paralelo(workers)


        print(f"\nWorkers: {workers}")


        for i, tiempo in enumerate(tiempos, 1):
            print(f"Prueba {i}: {tiempo:.6f} segundos")


        promedio = sum(tiempos) / PRUEBAS


        promedios[workers] = promedio


        print(f"Promedio: {promedio:.6f} segundos")




    # -----------------------------
    # SPEEDUP Y EFICIENCIA
    # -----------------------------


    print("\n===== SPEEDUP Y EFICIENCIA =====")


    # T1 = tiempo paralelo con 1 worker
    tiempo_base = promedios[1]


    speedups = {}
    eficiencias = {}


    for workers in workers_lista:


        tiempo_paralelo = promedios[workers]


        # Speedup = T1 / Tp
        speedup = tiempo_base / tiempo_paralelo


        # Eficiencia = Speedup / workers
        eficiencia = speedup / workers


        speedups[workers] = speedup
        eficiencias[workers] = eficiencia


        print(f"\nWorkers: {workers}")
        print(f"Speedup: {speedup:.6f}")
        print(f"Eficiencia: {eficiencia:.6f}")




    # -----------------------------
    # RESULTADOS FINALES
    # -----------------------------


    print("\n===== RESULTADOS FINALES =====")


    print(
        f"Tiempo secuencial: "
        f"{promedio_secuencial:.6f} segundos"
    )


    print(
        f"Tiempo paralelo con 1 worker (T1): "
        f"{tiempo_base:.6f} segundos"
    )


    for workers in workers_lista:


        print(
            f"{workers} workers: "
            f"{promedios[workers]:.6f} segundos"
        )




    # -----------------------------
    # GRÁFICA 1: TIEMPO
    # -----------------------------


    tiempos_grafica = [
        promedios[workers]
        for workers in workers_lista
    ]


    plt.figure()


    plt.plot(
        workers_lista,
        tiempos_grafica,
        marker="o"
    )


    plt.xlabel("Número de workers")
    plt.ylabel("Tiempo promedio (segundos)")
    plt.title("Workers vs Tiempo de ejecución")
    plt.xticks(workers_lista)
    plt.grid(True)


    plt.savefig("grafica_tiempo.png")


    plt.close()




    # -----------------------------
    # GRÁFICA 2: SPEEDUP
    # -----------------------------


    speedup_grafica = [
        speedups[workers]
        for workers in workers_lista
    ]


    plt.figure()


    plt.plot(
        workers_lista,
        speedup_grafica,
        marker="o"
    )


    plt.xlabel("Número de workers")
    plt.ylabel("Speedup")
    plt.title("Workers vs Speedup")
    plt.xticks(workers_lista)
    plt.grid(True)


    plt.savefig("grafica_speedup.png")


    plt.close()




    # -----------------------------
    # GRÁFICA 3: EFICIENCIA
    # -----------------------------


    eficiencia_grafica = [
        eficiencias[workers]
        for workers in workers_lista
    ]


    plt.figure()


    plt.plot(
        workers_lista,
        eficiencia_grafica,
        marker="o"
    )


    plt.xlabel("Número de workers")
    plt.ylabel("Eficiencia")
    plt.title("Workers vs Eficiencia")
    plt.xticks(workers_lista)
    plt.grid(True)


    plt.savefig("grafica_eficiencia.png")


    plt.close()




    print("\n===== GRÁFICAS GENERADAS =====")


    print("grafica_tiempo.png")
    print("grafica_speedup.png")
    print("grafica_eficiencia.png")




# -----------------------------
# EJECUCIÓN DEL PROGRAMA
# -----------------------------


if __name__ == "__main__":
    main()