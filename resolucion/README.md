# Resolución - Proyecto Integrador: CodeBase Q&A con IA

Este directorio contiene la implementación completa y funcional de la consigna.

## Estructura

- `backend/`: Código del backend con FastAPI, LangGraph y LlamaIndex.
- `frontend/`: Aplicación Next.js con interfaz generativa.

## Backend

1. Copia `.env.example` a `.env` y configura `OPENAI_API_KEY`.
2. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Genera el índice:
   ```bash
   python indexer.py
   ```
4. Inicia el servidor:
   ```bash
   uvicorn server:app --reload --port 8000
   ```
5. El endpoint estará disponible en `http://localhost:8000/api/ask`.

## Frontend

1. Ingresa al directorio `frontend/`.
2. Instala dependencias:
   ```bash
   npm install
   ```
3. Inicia la aplicación Next.js:
   ```bash
   npm run dev
   ```
4. Accede a `http://localhost:3000` en tu navegador para usar la interfaz.

## Ejemplos de uso

### Backend con cURL

```bash
curl -X POST http://localhost:8000/api/ask \
  -H "Content-Type: application/json" \
  -d '{"question":"¿Cómo se inicializa la base de datos?"}'
```

### Interfaz web

Escribe tu pregunta en el formulario y obtén la respuesta directamente en el navegador.
