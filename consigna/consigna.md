# Homework - Proyecto Integrador: CodeBase Q&A con IA

## Objetivos de Aprendizaje

- Integrar un frontend generativo (Next.js, v0.dev) con un backend inteligente (FastAPI, LlamaIndex, LangGraph) para construir una aplicación full-stack.
- Demostrar competencia en la arquitectura de aplicaciones de IA end-to-end, desde la ingesta de datos hasta la interfaz de usuario.
- Aplicar las mejores prácticas de desarrollo asistido por IA en un proyecto completo, utilizando herramientas para análisis, refactorización y testing.
- Implementar un sistema RAG funcional que indexe un repositorio de código y permita consultas semánticas.
- Construir un agente orquestador básico con LangGraph que interprete consultas y utilice el sistema RAG para generar respuestas contextualizadas.

## Consigna

### Contexto específico

Eres **Senior AI Engineer en Enterprise Code Solutions**, una empresa que desarrolla herramientas de análisis e inteligencia de código. Tu equipo de 8 desarrolladores necesita implementar un prototipo de sistema CodeBase Q&A que combine las tecnologías aprendidas en el curso: agentes inteligentes, RAG, frontend generativo y optimización de LLMs.

El proyecto está en fase de prototipo y necesitas crear un sistema básico que permita a desarrolladores hacer preguntas sobre un repositorio de código mediano (1K+ archivos), recibir análisis con navegación del código, y generar reportes automáticos básicos. Los usuarios son desarrolladores que necesitan entender codebases rápidamente.

## Datos disponibles

El proyecto incluye:

- **Repositorio de ejemplo**: 1,000+ archivos de código Python/JavaScript
- **Funcionalidades básicas**: Análisis de código, búsqueda semántica, reportes simples
- **Stack tecnológico**: LangGraph, LlamaIndex, Next.js, FastAPI
- **LLMs**: OpenAI GPT-4 (principal), Claude (fallback)
- **Base de datos**: SQLite local, ChromaDB para vectores

## Instrucciones paso a paso

**Paso 1: Configuración del sistema RAG básico**

- Configura LlamaIndex con el repositorio de ejemplo
- Implementa indexación básica de archivos de código
- Configura ChromaDB para almacenamiento de vectores
- Crea sistema de búsqueda semántica simple

**Paso 2: Implementación de agente básico**

- Crea un agente con LangGraph que analice consultas de código
- Implementa lógica para interpretar preguntas sobre arquitectura
- Añade capacidad de navegación básica por el código
- Configura generación de respuestas contextualizadas

**Paso 3: Frontend generativo básico**

- Crea interfaz Next.js simple para consultas
- Implementa componentes que se adapten al tipo de respuesta
- Añade visualización básica de resultados de búsqueda
- Configura navegación por archivos y funciones

**Paso 4: Optimización de LLMs**

- Implementa selección básica entre GPT-4 y Claude
- Configura fallback automático si un LLM falla
- Añade métricas básicas de costo y performance
- Optimiza prompts para diferentes tipos de consultas

**Paso 5: Testing y validación**

- Prueba el sistema con diferentes tipos de consultas
- Valida que las respuestas sean relevantes y útiles
- Verifica que el frontend se adapte correctamente
- Documenta el funcionamiento del prototipo

## Restricciones

- **Tiempo**: Máximo 2 horas de trabajo
- **Alcance**: Enfócate en funcionalidad básica, no en escalabilidad enterprise
- **Herramientas**: Usa herramientas gratuitas y configuración local
- **Funcionalidad**: El sistema debe ser funcional pero no crítico para producción

## Preguntas específicas

1. ¿Cómo configuraste el sistema RAG básico con LlamaIndex y ChromaDB?
2. ¿Qué estrategia implementaste para el agente de análisis de código?
3. ¿Cómo diseñaste el frontend generativo para adaptarse a diferentes respuestas?
4. ¿Qué optimizaciones de LLMs implementaste para el prototipo?
5. ¿Cómo validaste que el sistema integrado funcionara correctamente?

## Restricciones temporales

- **Tiempo máximo de ejecución**: 2 horas
- **Validación obligatoria**: Todo el contenido del homework debe ser completable en 2 horas de tiempo real
- **Consideraciones**: Incluir tiempo de configuración RAG (30 min), agente (35 min), frontend (30 min), optimización LLMs (15 min), testing (10 min)

## Material necesario

- **Archivos de datos**: Repositorio de código de ejemplo, configuraciones de LlamaIndex y ChromaDB
- **Scripts base**: Configuración de LangGraph, Next.js, FastAPI, ejemplos de agentes
- **Documentación**: Guías de integración, mejores prácticas de RAG, ejemplos de frontend generativo
- **Herramientas**: Python, Node.js, LangGraph, LlamaIndex, Next.js, FastAPI, ChromaDB
- **Recursos externos**: API keys de OpenAI y Anthropic, ejemplos de integración, casos de estudio

## Resolución sugerida

### Explicación paso a paso

**Paso 1: Configuración del sistema RAG básico**

- Instalación: `pip install llama-index chromadb`
- Configuración de LlamaIndex con `SimpleDirectoryReader`
- ChromaDB configurado con persistencia local
- Indexación básica de archivos Python/JavaScript del repositorio

**Paso 2: Implementación de agente básico**

- Agente LangGraph que interpreta consultas sobre código
- Lógica para identificar tipo de consulta (arquitectura, seguridad, calidad)
- Navegación básica por archivos y funciones relevantes
- Generación de respuestas contextualizadas con referencias al código

**Paso 3: Frontend generativo básico**

- Interfaz Next.js con formulario de consulta simple
- Componentes que se adaptan al tipo de respuesta (texto, código, lista)
- Visualización de resultados de búsqueda con snippets de código
- Navegación básica por archivos encontrados

**Paso 4: Optimización de LLMs**

- Selección automática: GPT-4 para consultas complejas, Claude para análisis
- Fallback automático si un LLM falla o excede límites
- Métricas básicas: tiempo de respuesta, costo por consulta
- Prompts optimizados para diferentes tipos de análisis

**Paso 5: Testing y validación**

- Pruebas con consultas típicas: "¿Cómo funciona la autenticación?", "¿Dónde se define la clase User?"
- Validación de relevancia de respuestas y referencias al código
- Verificación de adaptación del frontend a diferentes tipos de respuesta
- Documentación del prototipo funcional

## Justificación detallada

- **RAG básico** proporciona búsqueda semántica suficiente para un prototipo
- **Agente simple** demuestra conceptos de LangGraph sin complejidad excesiva
- **Frontend adaptativo** muestra capacidades de UI generativa
- **Optimización básica** enseña selección inteligente de LLMs

## Comentarios pedagógicos

- Este ejercicio integra todas las tecnologías del curso de manera práctica
- Demuestra cómo combinar RAG, agentes y frontend generativo
- Muestra la importancia de la optimización de LLMs en sistemas reales
- Enseña a crear prototipos funcionales en tiempo limitado

## Alternativas consideradas

- **Sistema complejo**: Demasiado para 2 horas, se enfocó en funcionalidad básica
- **Múltiples agentes**: Complejidad innecesaria para el tiempo disponible
- **Frontend estático**: No demuestra capacidades generativas del curso

## Checkpoints de autoevaluación

- [ ] ¿El sistema RAG puede encontrar código relevante para las consultas?
- [ ] ¿El agente interpreta correctamente diferentes tipos de preguntas?
- [ ] ¿El frontend se adapta apropiadamente a diferentes tipos de respuesta?
- [ ] ¿La optimización de LLMs funciona correctamente con fallback?
- [ ] ¿El tiempo total de ejecución fue menor a 2 horas?

## Criterios de Evaluación

La evaluación se basará en los siguientes puntos:

1.  **Funcionalidad del Sistema RAG (30%):**
    - El sistema RAG indexa correctamente el repositorio de código de ejemplo.
    - Las consultas semánticas devuelven fragmentos de código relevantes y precisos.
2.  **Orquestación del Agente (30%):**
    - El agente en LangGraph interpreta correctamente la intención del usuario.
    - El agente utiliza eficazmente el sistema RAG para formular respuestas contextualizadas y coherentes.
3.  **Integración Frontend-Backend (25%):**
    - La interfaz en Next.js se comunica correctamente con el backend de FastAPI.
    - El frontend visualiza las respuestas (texto y fragmentos de código) de manera clara y útil.
4.  **Optimización y Robustez (15%):**
    - Se implementa una estrategia básica de selección de LLM y fallback que funciona correctamente.
    - El sistema integrado es funcional y responde a consultas de prueba de manera consistente.
    - Las respuestas a las preguntas específicas demuestran una comprensión holística del proyecto.
