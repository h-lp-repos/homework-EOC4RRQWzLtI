# Consigna - Proyecto Integrador: CodeBase Q&A con IA

## Objetivos de Aprendizaje

- Integrar un frontend generativo (Next.js, v0.dev) con un backend inteligente (FastAPI, LlamaIndex, LangGraph) para construir una aplicación full-stack.
- Demostrar competencia en la arquitectura de aplicaciones de IA end-to-end, desde la ingesta de datos hasta la interfaz de usuario.
- Aplicar las mejores prácticas de desarrollo asistido por IA en un proyecto completo, utilizando herramientas para análisis, refactorización y testing.
- Implementar un sistema RAG funcional que indexe un repositorio de código y permita consultas semánticas.
- Construir un agente orquestador básico con LangGraph que interprete consultas y utilice el sistema RAG para generar respuestas contextualizadas.

## Consigna

Eres **Senior AI Engineer en Enterprise Code Solutions**, una consultora que desarrolla herramientas de análisis e inteligencia de código. Debes crear un prototipo de sistema CodeBase Q&A que permita a desarrolladores hacer preguntas en lenguaje natural sobre un repositorio de código y recibir análisis con contexto.

### Pasos principales

1. Configuración del sistema RAG básico (LlamaIndex + ChromaDB)
2. Implementación de agente básico (LangGraph)
3. Frontend generativo básico (Next.js, React, Tailwind CSS, shadcn/ui)
4. Optimización de LLMs (GPT-4, Claude)
5. Testing y validación

Consulta la especificación completa en el documento de la consigna.

## Datos de ejemplo

Este directorio incluye un pequeño conjunto de archivos de código de ejemplo en `sample-code/` para pruebas locales.

## Pistas

1. Configura primero la indexación de archivos antes de implementar el agente.
2. Usa componentes dinámicos en Next.js para renderizar distintos formatos de respuesta.

## Scaffolds

Este directorio contiene los archivos de scaffolding para comenzar la implementación:

- **indexer.py**: Esqueleto para configurar LlamaIndex y ChromaDB.
- **agent.py**: Esqueleto de agente con LangGraph.
- **server.py**: Scaffolding para servidor FastAPI.

Sigue esta consigna para implementar la solución completa.

## Requisitos

Instala las dependencias usando el archivo raíz:

```bash
pip install -r ../requirements.txt
```
