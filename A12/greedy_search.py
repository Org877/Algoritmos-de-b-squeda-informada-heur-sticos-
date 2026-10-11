import time
import heapq

def greedy_search(grafo: dict, origen: str, destino: str, limite_nodos: int) -> dict:
    start_time = time.perf_counter()
    
    # Cola de prioridad que almacena tuplas: (heuristica, nodo_actual, ruta_acumulada)
    # 
    # aquí implementamos una heurística genérica adaptable o basada en la distancia estimada).
    
    def heuristic(node, goal):
        # Heurística base puede ajustarse si se definen coordenadas. 
        # Si no hay coordenadas, se puede usar 0
        return 0 

    pq = []
    heapq.heappush(pq, (heuristic(origen, destino), origen, [origen]))
    
    visitados = set()
    max_memory = 0
    nodos_visitados_count = 0

    while pq:
        max_memory = max(max_memory, len(pq))
        if nodos_visitados_count >= limite_nodos:
            break

        _, actual, camino = heapq.heappop(pq)

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
                "t_n": round((end_time - start_time) * 1000, 4), # en ms
                "s_n": max_memory
            }

        for vecino, peso in grafo.get(actual, []):
            if vecino not in visitados:
                # En Greedy, priorizamos h(vecino)
                h_val = heuristic(vecino, destino)
                heapq.heappush(pq, (h_val, vecino, camino + [vecino]))

    end_time = time.perf_counter()
    return {
                "total_nodos_visitados": nodos_visitados_count,
                "solucion": True, 
                "ruta_solucion": camino,
                "t_n": round((end_time - start_time) * 1000, 4),
                "s_n": max_memory
    }