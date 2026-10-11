import time
import heapq

def star_search(grafo: dict, origen: str, destino: str, limite_nodos: int) -> dict:
    start_time = time.perf_counter()
    
    def heuristic(node, goal):
        return 0  # Heurística admisible genérica (puede calibrarse con coordenadas)

    # Cola de prioridad: (f_n, g_n, nodo_actual, ruta_acumulada)
    pq = []
    g_costs = {origen: 0}
    heapq.heappush(pq, (heuristic(origen, destino), 0, origen, [origen]))
    
    visitados = set()
    max_memory = 0
    nodos_visitados_count = 0

    while pq:
        max_memory = max(max_memory, len(pq))
        if nodos_visitados_count >= limite_nodos:
            break

        f, g, actual, camino = heapq.heappop(pq)

        if actual in visitados:
            continue

        visitados.add(actual)
        nodos_visitados_count += 1

        if actual == destino:
            end_time = time.perf_counter()
            return {
                "total_nodos_visitados": nodos_visitados_count,
                "solucion": True,
                "ruta_solucion": camino,
                "t_n": round((end_time - start_time) * 1000, 4),
                "s_n": max_memory
            }

        for vecino, peso in grafo.get(actual, []):
            nuevo_g = g + peso

            if vecino not in g_costs or nuevo_g < g_costs[vecino]:
                g_costs[vecino] = nuevo_g
                f_n = nuevo_g + heuristic(vecino, destino)
                heapq.heappush(pq, (f_n, nuevo_g, vecino, camino + [vecino]))

    end_time = time.perf_counter()
    return {
        "total_nodos_visitados": nodos_visitados_count,
        "solucion": False,  
        "ruta_solucion": [],
        "t_n": round((end_time - start_time) * 1000, 4),
        "s_n": max_memory
    }
