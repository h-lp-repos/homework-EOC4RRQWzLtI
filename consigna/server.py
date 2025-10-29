"""Servidor FastAPI para exponer el agente"""

# Requerimientos de instalación:
# pip install fastapi uvicorn

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import query_agent

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str

@app.post("/query", response_model=QueryResponse)
def query_endpoint(request: QueryRequest):
    """
    Endpoint para consultar al agente de CodeBase Q&A.

    Usage:
    curl -X POST http://localhost:8000/query \
         -H 'Content-Type: application/json' \
         -d '{"question":"¿Cómo funciona la base de datos?"}'
    """
    try:
        answer = query_agent(request.question, index_path="path/to/index")
        return QueryResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Para ejecutar el servidor:
# uvicorn consigna.server:app --reload --port 8000
