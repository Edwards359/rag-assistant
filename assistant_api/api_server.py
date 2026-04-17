"""
HTTP API для RAG Assistant — интеграция с n8n и другими системами.

Эндпоинты:
  GET  /health  — проверка доступности
  POST /query   — RAG-запрос: { "query": "вопрос" } → { "answer", "from_cache", ... }
"""

import os
import sys
from pathlib import Path

# Загрузка .env из корня проекта (Per08)
root = Path(__file__).resolve().parent.parent
env_path = root / ".env"
if env_path.exists():
    from dotenv import load_dotenv
    load_dotenv(env_path)

# Инициализация после загрузки .env
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="RAG Assistant API",
    description="API для RAG-запросов. Совместим с n8n (Webhook → HTTP Request).",
    version="1.0.0",
)


class QueryRequest(BaseModel):
    """Тело запроса для /query."""
    query: str = Field(..., min_length=1, description="Вопрос к RAG-ассистенту")


class QueryResponse(BaseModel):
    """Ответ /query."""
    query: str
    answer: str
    from_cache: bool
    model: str | None = None
    sources_count: int = 0


# Глобальный pipeline (ленивая инициализация при первом /query)
_pipeline = None


def _get_pipeline():
    global _pipeline
    if _pipeline is None:
        if not os.getenv("OPENAI_API_KEY"):
            raise HTTPException(
                status_code=503,
                detail="OPENAI_API_KEY не задан. Добавьте в .env и перезапустите сервер.",
            )
        from rag_pipeline import RAGPipeline
        data_file = Path(__file__).parent / "data" / "docs.txt"
        _pipeline = RAGPipeline(
            collection_name="api_rag_collection",
            cache_db_path="api_rag_cache.db",
            data_file=str(data_file),
            model=os.getenv("RAG_MODEL", "gpt-4o-mini"),
        )
    return _pipeline


@app.get("/health")
def health():
    """Проверка доступности сервиса."""
    return {"status": "ok", "service": "rag-assistant-api"}


@app.post("/query", response_model=QueryResponse)
def query(req: QueryRequest):
    """
    RAG-запрос: поиск по базе знаний и генерация ответа (с кешем).
    Подходит для вызова из n8n: Webhook (POST JSON) → HTTP Request сюда → Respond.
    """
    try:
        pl = _get_pipeline()
        result = pl.query(req.query.strip(), use_cache=True)
        return QueryResponse(
            query=result["query"],
            answer=result["answer"],
            from_cache=result["from_cache"],
            model=result.get("model"),
            sources_count=len(result.get("context_docs") or []),
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    host = os.getenv("RAG_API_HOST", "0.0.0.0")
    port = int(os.getenv("RAG_API_PORT", "8000"))
    uvicorn.run(app, host=host, port=port)
