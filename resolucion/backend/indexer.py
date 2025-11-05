#!/usr/bin/env python3
"""
Indexer: build semantic index for code repository using LlamaIndex and ChromaDB.
"""

import os
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex
from chromadb.config import Settings
import chromadb


def build_index(data_dir: str, persist_dir: str = ".chromadb"):
    """Build and persist semantic index from data_dir to persist_dir."""
    # Initialize ChromaDB client
    client = chromadb.Client(Settings(
        chroma_db_impl="duckdb+parquet", persist_directory=persist_dir
    ))
    # Load documents
    documents = SimpleDirectoryReader(data_dir).load_data()
    # Create index
    index = GPTVectorStoreIndex.from_documents(
        documents, chroma_db_config={"persist_directory": persist_dir}
    )
    # Persist index
    index.storage_context.persist()
    print(f"Index built and persisted to {persist_dir}")


if __name__ == "__main__":
    here = os.path.dirname(__file__)
    sample_code_path = os.path.abspath(
        os.path.join(here, "../../consigna/sample-code")
    )
    build_index(sample_code_path)
