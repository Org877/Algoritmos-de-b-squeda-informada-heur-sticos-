from typing import Dict, List, Tuple, Optional 
from pydantic import BaseModel, Field

class SearchRequest(BaseModel):
    grafo: Dict[str, List[Tuple[str, float]]] = Field(..., description="Adyacencia con pesos grafo")
    origen: str = Field(..., description= "Nodo inicio")
    destino: str = Field(..., description= "Nodo objetivo")
    limite_nodos: Optional[int] = Field(None, description= "Limite maximo de nodos a visitar")

class SearchResponse(BaseModel):
    total_nodos_visitados: int
    solucion: bool
    ruta_solucion: List[str]
    t_n: float #Tiempo de ejecucion 
    s_n: int   #Complejidad espacial 