# 🤖 RAG Ассистенты - Проект Per08

Два консольных RAG-ассистента с разными языковыми моделями для работы с базой знаний.

---

## 📁 Структура проектов

### 🔵 assistant_api - RAG с OpenAI API
- **LLM:** GPT-4o-mini
- **Embeddings:** text-embedding-3-small (OpenAI)
- **Особенности:** Оценка качества через RAGAS

### 🟢 assistant_giga - RAG с GigaChat
- **LLM:** GigaChat (Сбер)
- **Embeddings:** GigaChat Embeddings API
- **Особенности:** Работа с российским LLM

---

## 🚀 Быстрый старт

### 1. Активация виртуального окружения

**PowerShell:**
```powershell
.\activate.ps1
```

**CMD:**
```cmd
activate.bat
```

**Или вручную:**
```powershell
.\venv_py311\Scripts\activate
```

### 2. Настройка переменных окружения

Создайте файл `.env` в корне проекта:

**Для assistant_api:**
```env
OPENAI_API_KEY=your-openai-api-key
```

**Для assistant_giga:**
```env
GIGACHAT_AUTH_KEY=your-basic-auth-token
GIGACHAT_RQUID=your-request-uid
```

### 3. Запуск ассистентов

**OpenAI ассистент:**
```powershell
cd assistant_api
python app.py
```

**GigaChat ассистент:**
```powershell
cd assistant_giga
python app.py
```

---

## 🎯 Возможности

### Консольные команды:
- `exit` / `quit` / `q` - выход из приложения
- `stats` - показать статистику системы
- `clear` - очистить кеш (с подтверждением)

### Функциональность:
✅ **Семантический поиск** в базе знаний (ChromaDB)  
✅ **Кеширование** ответов (SQLite)  
✅ **Smart Chunking** с overlap для сохранения контекста  
✅ **Статистика** использования (кеш, векторная БД)  
✅ **Красивый вывод** с эмодзи и форматированием  

---

## 📊 Оценка качества RAG системы

Только для `assistant_api` (доступен модуль RAGAS):

```powershell
cd assistant_api
python evaluate_ragas.py
```

**Метрики:**
- **Faithfulness** - точность ответа относительно контекста
- **Context Precision** - качество извлечённого контекста

---

## 🛠️ Технологии

- **Python:** 3.11.0
- **LLM:** OpenAI GPT-4o-mini / GigaChat
- **Vector DB:** ChromaDB 1.4.0
- **Embeddings:** OpenAI / GigaChat
- **Framework:** LangChain 1.2.3
- **Evaluation:** RAGAS 0.4.2
- **Cache:** SQLite

---

## 📚 База знаний

Файл: `assistant_api/data/docs.txt` и `assistant_giga/data/docs.txt`

**Темы:**
- Машинное обучение
- Нейронные сети и Deep Learning
- NLP и трансформеры
- Word embeddings
- RAG системы
- Векторные базы данных
- Prompt engineering
- Fine-tuning
- Метрики качества LLM
- Кеширование в AI
- Chunking стратегии
- Температура в LLM
- Token limits
- Semantic search

---

## 🔧 Архитектура RAG Pipeline

```
Запрос пользователя
    ↓
Проверка кеша (SQLite)
    ↓
Если нет в кеше:
    ↓
Семантический поиск (ChromaDB)
    ↓
Формирование промпта с контекстом
    ↓
Генерация ответа (LLM)
    ↓
Сохранение в кеш
    ↓
Вывод результата
```

### Параметры Chunking:
- **Chunk size:** 500 символов
- **Overlap:** 100 символов
- **Стратегия:** приоритет абзацам, разбиение по предложениям
- **Минимум:** 50 символов

### Параметры LLM:
- **Temperature:** 0.3 (низкая для точности)
- **Max tokens:** 500
- **Top K documents:** 3

---

## 📦 Установленные пакеты

Основные зависимости (всего установлено 150+ пакетов):

```
openai              2.15.0
chromadb            1.4.0
langchain           1.2.3
langchain-openai    1.1.7
ragas               0.4.2
sentence-transformers 5.2.0
pandas              2.3.3
numpy               2.4.1
datasets            4.4.2
python-dotenv       1.2.1
```

---

## 💡 Примеры использования

### Пример сессии:

```
💭 Ваш вопрос: Что такое RAG?

────────────────────────────────────────────────────────────
📝 Вопрос: Что такое RAG?
────────────────────────────────────────────────────────────
🌐 Источник: OpenAI API (gpt-4o-mini)
   Использовано документов: 3

💬 Ответ:
RAG (Retrieval-Augmented Generation) - это подход, который 
комбинирует извлечение информации из базы знаний с генерацией 
текста языковыми моделями...

📚 Использованный контекст:
   1. RAG (Retrieval-Augmented Generation) - это подход, который 
      комбинирует извлечение информации...
────────────────────────────────────────────────────────────
```

---

## 🔍 Troubleshooting

### Проблема: "OPENAI_API_KEY не установлен"
**Решение:** Создайте файл `.env` в корне проекта с ключом API

### Проблема: "ModuleNotFoundError"
**Решение:** Убедитесь, что виртуальное окружение активировано:
```powershell
.\venv_py311\Scripts\activate
```

### Проблема: Медленная работа
**Решение:** Используйте кеш - повторные запросы берутся из SQLite без вызова API

---

## 📈 Производительность

- **Первый запрос:** 2-5 секунд (поиск + LLM)
- **Повторный запрос:** <100ms (из кеша)
- **Chunking:** ~30 чанков для базы знаний
- **Размер кеша:** зависит от количества запросов

---

## 📚 Дополнительная документация

- **[OpenAI Assistant Info](assistant_api/OPENAI_INFO.md)** - подробная информация об OpenAI ассистенте
- **[GigaChat Assistant Info](assistant_giga/GIGACHAT_INFO.md)** - особенности работы с GigaChat API

---

## 🎓 Автор

Проект создан для демонстрации RAG систем с разными LLM бэкендами.

**Python версия:** 3.11.9 ✅ (обновлено)  
**Последнее обновление:** Январь 2026
