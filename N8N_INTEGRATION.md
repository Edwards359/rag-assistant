# Интеграция RAG Assistant с n8n

RAG Assistant можно вызывать из [n8n](https://n8n.io) через HTTP API: n8n передаёт вопрос в RAG API и возвращает ответ во внешние системы (Telegram, веб, почта и т.п.).

---

## 1. Запуск RAG API

Из корня проекта:

```bash
# Активация окружения
.\venv_py311\Scripts\Activate.ps1   # Windows
# source venv_py311/bin/activate     # Linux/Mac

# Установка зависимостей (если ещё не ставили)
pip install fastapi "uvicorn[standard]"

# Запуск API (из папки assistant_api)
cd assistant_api
python -m uvicorn api_server:app --host 0.0.0.0 --port 8000
```

Проверка: в браузере `http://localhost:8000/health` → `{"status":"ok",...}`.

В `.env` должен быть `OPENAI_API_KEY`.

---

## 2. Запуск n8n

### Вариант A: Docker (рекомендуется)

```bash
# Из корня Per08
docker compose -f docker-compose.n8n.yml up -d
```

n8n: **http://localhost:5678**

Переменная `RAG_API_URL=http://host.docker.internal:8000` уже задана в `docker-compose.n8n.yml` для доступа с контейнера к API на хосте.

**Linux:** если `host.docker.internal` не работает, в `docker-compose.n8n.yml` раскомментируйте:

```yaml
extra_hosts:
  - "host.docker.internal:host-gateway"
```

или в `environment` задайте, например:  
`RAG_API_URL=http://172.17.0.1:8000`.

### Вариант B: n8n установлен на хосте

Если n8n стоит рядом с RAG API на одной машине, по умолчанию подойдёт `http://localhost:8000`. В n8n можно задать переменную окружения `RAG_API_URL`, если порт другой.

---

## 3. Импорт workflow в n8n

1. Откройте n8n: http://localhost:5678  
2. **Workflows** → **Import from File** или **Add workflow** → **Import from URL/File**.  
3. Укажите файл:  
   `n8n/workflow-rag-query.json`  
4. Сохраните workflow и включите его (**Active**).

---

## 4. Workflow «RAG Assistant - Query»

Цепочка: **Webhook** → **Parse Query** → **RAG API: Query** → **Respond to Webhook**.

- **Webhook**  
  - Метод: `POST`  
  - Path: `rag-query`  
  - Production URL: `http://localhost:5678/webhook/rag-query`  
  - Test: `http://localhost:5678/webhook-test/rag-query`

- **Тело запроса** (JSON):

  ```json
  { "query": "Что такое RAG?" }
  ```

  Также принимаются поля `question` или `q`.

- **Ответ** (от RAG API):

  ```json
  {
    "query": "Что такое RAG?",
    "answer": "RAG (Retrieval-Augmented Generation) — это...",
    "from_cache": false,
    "model": "gpt-4o-mini",
    "sources_count": 3
  }
  ```

---

## 5. Проверка через curl

```bash
# RAG API напрямую
curl -X POST http://localhost:8000/query -H "Content-Type: application/json" -d "{\"query\": \"Что такое RAG?\"}"

# Через n8n (после активации workflow)
curl -X POST "http://localhost:5678/webhook/rag-query" -H "Content-Type: application/json" -d "{\"query\": \"Что такое RAG?\"}"
```

---

## 6. Использование в других workflow n8n

- Узел **HTTP Request**:  
  - URL: `http://localhost:8000/query` (или `{{ $env.RAG_API_URL }}/query`)  
  - Method: `POST`  
  - Body (JSON): `{"query": "вопрос"}`  
- Или триггер **Webhook** `rag-query` и дальше по цепочке, как в `workflow-rag-query.json`.

Так RAG можно встраивать в сценарии: Telegram-боты, формы, автоматические отчёты, пайпы с другими сервисами.

---

## 7. Переменные окружения

| Переменная      | Где        | Описание |
|-----------------|------------|----------|
| `OPENAI_API_KEY`| RAG API    | Ключ OpenAI (обязательно). |
| `RAG_API_HOST`  | RAG API    | Хост (по умолчанию `0.0.0.0`). |
| `RAG_API_PORT`  | RAG API    | Порт (по умолчанию `8000`). |
| `RAG_API_URL`   | n8n (Docker) | URL RAG API, например `http://host.docker.internal:8000`. |
| `RAG_MODEL`     | RAG API    | Модель OpenAI (по умолчанию `gpt-4o-mini`). |

---

## 8. Файлы

| Файл | Назначение |
|------|------------|
| `assistant_api/api_server.py`     | FastAPI: `GET /health`, `POST /query`. |
| `n8n/workflow-rag-query.json`     | Workflow n8n для RAG-запросов. |
| `docker-compose.n8n.yml`          | Запуск n8n в Docker с `RAG_API_URL`. |
| `N8N_INTEGRATION.md`              | Эта инструкция. |
