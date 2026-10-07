Proyecto Práctico HPCDescripción

Este proyecto compara el procesamiento secuencial y paralelo de un conjunto de 100,000 datos utilizando Python. Se realiza una operación matemática sobre cada dato y se mide el tiempo de ejecución para analizar el comportamiento del procesamiento paralelo.

La operación utilizada es:

f(x) = sqrt(x) + x² + sin(x) + cos(x) + log(x)

Tecnologías utilizadas

Python

ProcessPoolExecutor

Matplotlib

Git

GitHub

Procesamiento secuencial

El procesamiento secuencial realiza las operaciones una por una utilizando un solo flujo de ejecución.

Se procesaron 100,000 datos y se realizaron tres pruebas.

El tiempo promedio obtenido fue:

0.046579 segundos

Procesamiento paralelo

Para el procesamiento paralelo se utilizó ProcessPoolExecutor.

Se realizaron pruebas utilizando:

1 worker

2 workers

4 workers

Cada configuración se ejecutó tres veces y se calculó su promedio.





Workers

Tiempo promedio

1

46.140154 s

2

43.975841 s

4

43.112863 sSpeedup y eficiencia

Para calcular el Speedup se utilizó como T1 el tiempo del procesamiento paralelo con 1 worker.





Workers

Speedup

Eficiencia

1

1.000000

1.000000

2

1.049216

0.524608

4

1.070218

0.267554Análisis de resultados¿El procesamiento paralelo fue más rápido?

Sí. Dentro de las pruebas de procesamiento paralelo, el mejor resultado se obtuvo utilizando 4 workers, con un tiempo promedio de 43.112863 segundos.

Sin embargo, al comparar con el procesamiento secuencial, que tuvo un tiempo promedio de 0.046579 segundos, el procesamiento secuencial fue mucho más rápido.

Esto se debe principalmente al costo de crear procesos y distribuir 100,000 tareas individuales entre ellos.

¿Qué configuración obtuvo el menor tiempo?

La configuración de 4 workers obtuvo el menor tiempo entre las pruebas paralelas:

43.112863 segundos.

¿Duplicar los workers duplicó el rendimiento?

No. Al pasar de 1 a 2 workers, el tiempo disminuyó de 46.140154 a 43.975841 segundos.

Al aumentar de 2 a 4 workers, el tiempo volvió a disminuir ligeramente hasta 43.112863 segundos.

El rendimiento no se duplicó porque existe un costo asociado con la creación de procesos, comunicación y distribución de las tareas.

¿Por qué el problema es paralelizable?

El problema es paralelizable porque cada dato puede procesarse de manera independiente. El cálculo realizado sobre un dato no depende del resultado de los demás datos.

Por esta razón, diferentes procesos pueden trabajar sobre diferentes elementos al mismo tiempo.

¿Cuándo deja de ayudar agregar más workers?

Agregar más workers deja de ser beneficioso cuando el costo de administrar los procesos y distribuir las tareas es mayor que la ganancia obtenida por ejecutar operaciones simultáneamente.

En este experimento, aumentar de 2 a 4 workers solamente produjo una mejora pequeña.

¿Qué limitaciones de hardware pueden afectar?

El rendimiento puede verse afectado por:

Número de núcleos disponibles del procesador.

Memoria RAM.

Carga de otros programas en el equipo.

Capacidad del sistema operativo para administrar procesos.

Costo de comunicación entre procesos.

¿Este proyecto representa HPC?

El proyecto aplica principios de Cómputo de Alto Rendimiento, especialmente la ejecución paralela, medición de tiempos, Speedup y eficiencia.

Sin embargo, no representa un sistema HPC completo porque se ejecuta en un equipo convencional y no en un clúster de múltiples nodos.

El proyecto sirve como una demostración práctica de conceptos fundamentales de HPC.

Gráficas

El proyecto genera automáticamente tres gráficas:

grafica\_tiempo.png — Workers vs tiempo de ejecución.

grafica\_speedup.png — Workers vs Speedup.

grafica\_eficiencia.png — Workers vs eficiencia.

Ejecución

Para ejecutar las mediciones:

python mediciones.py

El programa realiza tres pruebas para cada configuración de workers y genera las gráficas automáticamente.

Estructura del proyecto

proyecto-hpc/

│

├── main.py

├── paralelo.py

├── mediciones.py

├── grafica\_tiempo.png

├── grafica\_speedup.png

├── grafica\_eficiencia.png

└── README.md

Integrantes

Elizabeth

Diana

Mauricio

