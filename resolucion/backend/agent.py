#!/usr/bin/env python3
"""
Agent: uses LangGraph to query the vector index.
"""

import os
from llama_index import LLMPredictor, ServiceContext, GPTVectorStoreIndex
from langgraph import Agent, Tool, ToolMetadata


def create_agent(index_dir: str = ".chromadb"):
    """Create and return an agent connected to the semantic index."""
    # Load existing index
    index = GPTVectorStoreIndex.load_from_disk(os.path.join(index_dir, "storage.json"))
    # Initialize LLM predictor and service context
    llm_predictor = LLMPredictor()
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
    # Define a tool for querying the index
    def query_tool(query: str) -> str:
        return index.as_query_engine(service_context=service_context).query(query)
    tool = Tool(
        fn=query_tool,
        metadata=ToolMetadata(name="code_query", description="Answer questions about the codebase")
    )
    # Create agent with the tool
    agent = Agent(tools=[tool])
    return agent


if __name__ == "__main__":
    agent = create_agent()
    question = "¿Cómo se inicializa la base de datos?"
    answer = agent.run(question=question)
    print(answer)
