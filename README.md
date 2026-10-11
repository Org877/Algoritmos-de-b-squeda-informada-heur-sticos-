# Algoritmos-de-b-squeda-informada-heur-sticos-
# Actividad 12: Implementación y Evaluación de Algoritmos de Búsqueda Informada (Greedy y A*)


* **** Universidad Iberoamericana Puebla
* **Trabajo** Actividad 12 - Búsqueda Informada

---

##  Descripción del Proyecto
Este proyecto implementa una API REST de alto rendimiento utilizando **FastAPI** para resolver problemas de enrutamiento y búsqueda en grafos mediante algoritmos informados (**Greedy Best-First Search** y **A\***).

* **FastAPI & Uvicorn:** Servidor web encargado de exponer los endpoints (`/search/greedy` y `/search/star`) y proveer la documentación interactiva en Swagger UI (`/docs`).
* **Pydantic:** Utilizado para la validación estricta de esquemas y tipos de datos en los payloads JSON de entrada y salida.
* **Algoritmos de Búsqueda:** Implementados en Python puro haciendo uso de colas de prioridad (`heapq`) para optimizar la selección de nodos, control de memoria y cálculo de métricas de desempeño.

---

##  Endpoints Disponibles
1. **POST `/search/greedy`**: Ejecuta la búsqueda voraz informada basada únicamente en la heurística.
2. **POST `/search/star`**: Ejecuta la búsqueda A* combinando el costo real acumulado $g(n)$ y la heurística $h(n)$.

---

##  Resultados Experimentales

La siguiente tabla recopila las métricas obtenidas durante las pruebas empíricas realizadas en los tres escenarios de grafos requeridos:

| Escenario (Grafo) | Algoritmo | Nodos Visitados | ¿Solución? | Ruta de Solución | Tiempo ($T(n)$ en ms) | Espacio ($S(n)$ en memoria) |
| :--- | :--- | :---: | :---: | :--- | :---: | :---: |
| **10 Nodos** (`A` $\to$ `J`) | Greedy | 10 | Sí | `["A", "B", "E", "H", "J"]` | 0.0599 | 7 |
| **10 Nodos** (`A` $\to$ `J`) | A\* | 10 | Sí | `["A", "B", "F", "I", "J"]` | 0.1202 | 6 |
| **25 Nodos** (`A` $\to$ `Y`) | Greedy | 25 | Sí | `["A", "B", "D", "E", "C", "I", "M", "P", "X", "Y"]` | 0.1525 | 11 |
| **25 Nodos** (`A` $\to$ `Y`) | A\* | 21 | Sí | `["A", "D", "F", "K", "R", "U", "Y"]` | 0.1118 | 10 |
| **50 Nodos** (`A` $\to$ `AX`) | Greedy | 15 | Sí | `["A", "C", "K", "R", "AD", "AM", "AV", "AX"]` | 0.0780 | 6 |
| **50 Nodos** (`A` $\to$ `AX`) | A\* | 20 | Sí | `["A", "F", "K", "R", "AD", "AM", "AV", "AX"]` | 0.0940 | 5 |

---

##  Análisis Comparativo y Conclusiones

* **Estrategia de Exploración:** Greedy tiende a priorizar de forma directa los nodos más cercanos a la meta según la heurística local, lo que le permite en ocasiones explorar menos nodos en grafos amplios, aunque sin garantizar optimalidad estricta. En contraste, A* evalúa tanto el costo acumulado como la estimación (`f(n) = g(n) + h(n)`), logrando caminos altamente eficientes y equilibrados (como se evidencia en el grafo de 25 nodos).
* **Rendimiento Computacional:** Gracias al uso de estructuras de datos nativas optimizadas como `heapq`, los tiempos de respuesta ($T(n)$) se mantienen consistentemente en el orden de las centésimas de milisegundo, y el uso máximo de memoria en la frontera ($S(n)$) permanece sumamente controlado en todos los casos de prueba.

---
