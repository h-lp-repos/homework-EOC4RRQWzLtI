"""Esqueleto para configurar LlamaIndex y ChromaDB"""

# Requerimientos de instalación:
# pip install llama-index chromadb

def build_index(repo_path: str, index_path: str = "index"):
    """
    Construye un índice semántico del repositorio de código.

    Args:
        repo_path (str): Ruta al directorio del repositorio a indexar.
        index_path (str): Ruta donde se guardará el índice generado.
    """
    # 1. Recorrer archivos del repositorio (pseudocódigo)
    #    for file in walk(repo_path):
    #        # Crear documento a partir del contenido de file
    #        pass
    #
    # 2. Configurar LlamaIndex para ingestar documentos
    #    # from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex
    #
    # 3. Guardar/serializar el índice en index_path
    #    # index.save_to_disk(index_path)
    pass

if __name__ == "__main__":
    # Ejemplo de uso:
    # build_index("path/to/tu/repositorio", index_path="path/to/index")
    build_index("path/to/tu/repositorio")
