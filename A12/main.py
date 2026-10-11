from fastapi import FastAPI
from schemas import SearchRequest, SearchResponse
from greedy_search import greedy_search
from star_search import star_search

app = FastAPI(title="API de Búsqueda Informada en Grafos", version="1.0.0")

@app.post("/search/greedy", response_model=SearchResponse)
def run_greedy(body: SearchRequest):
    total_nodos = len(body.grafo)
    limite = body.limite_nodos if body.limite_nodos is not None else int(total_nodos * 0.8)
    resultado = greedy_search(body.grafo, body.origen, body.destino, limite)
    return resultado

@app.post("/search/star", response_model=SearchResponse)
def run_star(body: SearchRequest):
    total_nodos = len(body.grafo)
    limite = body.limite_nodos if body.limite_nodos is not None else int(total_nodos * 0.8)
    resultado = star_search(body.grafo, body.origen, body.destino, limite)
    return resultado