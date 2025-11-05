#!/usr/bin/env python3
"""
Server: FastAPI application exposing the QA endpoint.
"""

import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import create_agent

app = FastAPI(title="CodeBase Q&A API")

# Allow CORS from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str

# Load agent once
INDEX_DIR = os.getenv("INDEX_DIR", ".chromadb")
agent = create_agent(INDEX_DIR)

@app.post("/api/ask", response_model=QueryResponse)
def ask_question(request: QueryRequest):
    try:
        answer = agent.run(question=request.question)
        return QueryResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
