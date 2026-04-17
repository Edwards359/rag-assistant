## 🇷🇺 Обзор для заказчика

**RAG Assistant** — AI‑ассистент, который отвечает на вопросы по вашим документам и базе знаний.

- **Для чего:** уменьшить количество рутинных запросов к экспертам и поддержке.
- **Что делает:** ищет нужные фрагменты в документах и формирует понятный ответ с опорой на исходный текст.
- **Где полезен:** внутренние базы знаний, регламенты, инструкции, FAQ, справочники и техническая документация.
- **Пример кейса:** сотрудник задаёт вопрос по процедуре → ассистент возвращает ответ + выдержки из актуального документа.

---

# 🤖 RAG Assistant — две реализации

<div align="center">

[![CI](https://github.com/Edwards359/rag-assistant/actions/workflows/ci.yml/badge.svg)](https://github.com/Edwards359/rag-assistant/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.12.0-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991.svg)
![GigaChat](https://img.shields.io/badge/GigaChat-Sber-orange.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success.svg)

**Два production-ready RAG-ассистента (Retrieval-Augmented Generation) с разными LLM-бэкендами**

[Возможности](#-возможности) • [Установка](#-установка) • [Использование](#-использование) • [Документация](#-документация) • [Вклад](#-вклад-в-проект)

</div>

---

## 📋 Оглавление

- [О проекте](#-о-проекте)
- [Архитектура](#-архитектура)
- [Возможности](#-возможности)
- [Технологии](#-технологии)
- [Установка](#-установка)
- [Конфигурация](#-конфигурация)
- [Использование](#-использование)
- [Структура проекта](#-структура-проекта)
- [Документация](#-документация)
- [Производительность](#-производительность)
- [Решение проблем](#-решение-проблем)
- [Вклад в проект](#-вклад-в-проект)
- [Лицензия](#-лицензия)
- [Благодарности](#-благодарности)

---

## 🎯 О проекте

Проект демонстрирует две полноценные реализации RAG (Retrieval-Augmented Generation) с разными бэкендами больших языковых моделей:

### 🔵 Реализация на OpenAI (`assistant_api`)

- **LLM:** GPT-4o-mini
- **Эмбеддинги:** text-embedding-3-small
- **Оценка качества:** метрики RAGAS
- **Статус:** ✅ полностью работоспособна

### 🟢 Реализация на GigaChat (`assistant_giga`)

- **LLM:** GigaChat от Сбера
- **Эмбеддинги:** GigaChat Embeddings API (с fallback)
- **Статус:** ✅ работает с ограничениями

Общая инфраструктура:

- **Векторная БД:** ChromaDB
- **Кеш:** SQLite
- **Умный чанкинг:** семантическое разбиение текста с перекрытием
- **Консольный интерфейс:** интерактивный CLI

---

## 🏗️ Архитектура

```text
┌───────────────────────┐
│  Запрос пользователя  │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│    Проверка кеша      │ ◄─── SQLite
│     (SHA-256 хеш)     │
└──────────┬────────────┘
           │
     ┌─────┴─────┐
     │  Попал?  │
     └─┬──────┬──┘
    Да │      │ Нет
       │      ▼
       │  ┌────────────────────┐
       │  │  Векторный поиск   │ ◄─── ChromaDB
       │  │     (Top-K=3)      │
       │  └─────────┬──────────┘
       │            │
       │            ▼
       │  ┌────────────────────┐
       │  │  Сборка контекста  │
       │  │  (промпт + доки)   │
       │  └─────────┬──────────┘
       │            │
       │            ▼
       │  ┌────────────────────┐
       │  │   Генерация LLM    │ ◄─── OpenAI / GigaChat
       │  │  (Temperature=0.3) │
       │  └─────────┬──────────┘
       │            │
       │            ▼
       │  ┌────────────────────┐
       │  │    Запись в кеш    │
       │  └─────────┬──────────┘
       │            │
       └────────────┘
                │
                ▼
        ┌───────────────┐
        │     Ответ     │
        └───────────────┘
```

---

## ✨ Возможности

### Основной функционал

- **✅ Семантический поиск** — поиск релевантного контекста через векторные эмбеддинги
- **✅ Умный кеш** — мгновенные ответы на повторные запросы (<100 мс)
- **✅ Интеллектуальный чанкинг** — семантическое разбиение текста с перекрытием
- **✅ Два LLM-бэкенда** — выбор между OpenAI и GigaChat
- **✅ Метрики качества** — оценка через RAGAS для реализации на OpenAI
- **✅ Консольный интерфейс** — удобный CLI с командами
- **✅ Статистика** — попадания в кеш, количество документов, производительность

### Расширенные возможности

- **Сохранение контекста** — перекрытие чанков поддерживает связность
- **Нормализация запросов** — кеш нечувствителен к регистру и пробелам
- **Автоматический ретрай** — обновление OAuth-токена для GigaChat
- **Fallback-эмбеддинги** — хеш-векторы, когда API недоступен
- **Подробное логирование** — отслеживание всех шагов pipeline
- **Интеграция с n8n** — HTTP API (`POST /query`) и готовый n8n workflow для автоматизации

---

## 🛠️ Технологии

### Основные

| Технология | Версия | Назначение |
| ---------- | ------ | ---------- |
| **Python** | 3.12.0 | Среда выполнения |
| **OpenAI API** | 2.15.0 | LLM и эмбеддинги (assistant_api) |
| **GigaChat API** | — | Русскоязычный LLM (assistant_giga) |
| **ChromaDB** | 1.4.0 | Векторная база |
| **LangChain** | 1.2.3 | Фреймворк для LLM |
| **RAGAS** | 0.4.2 | Оценка качества RAG |

### Вспомогательные библиотеки

```python
sentence-transformers  # 5.2.0  — трансформерные модели
numpy                  # 2.4.1  — численные операции
pandas                 # 2.3.3  — работа с данными
tiktoken               # 0.12.0 — подсчёт токенов
python-dotenv          # 1.2.1  — работа с переменными окружения
```

---

## 📥 Установка

### Требования

- **Python 3.12+** (проверено на 3.12.0)
- **Git**
- **Ключ OpenAI API** (для `assistant_api`)
- **Учётные данные GigaChat** (для `assistant_giga`)

### Быстрый старт

```bash
# Клонировать репозиторий
git clone https://github.com/Edwards359/rag-assistant.git
cd rag-assistant

# Создать виртуальное окружение
py -3.12 -m venv venv_py312

# Активировать (Windows PowerShell)
.\venv_py312\Scripts\Activate.ps1

# Активировать (Windows CMD)
.\venv_py312\Scripts\activate.bat

# Активировать (Linux/Mac)
source venv_py312/bin/activate

# Установить зависимости
pip install -r requirements.txt

# Настроить переменные окружения
copy env.example .env
# Отредактируйте .env — добавьте свои API-ключи
```

### Альтернатива: через скрипты активации

```bash
# Windows PowerShell
.\activate.ps1

# Windows CMD
activate.bat
```

---

## ⚙️ Конфигурация

### Переменные окружения

Создайте файл `.env` в корне проекта:

```env
# Настройки OpenAI (обязательно для assistant_api)
OPENAI_API_KEY=sk-your-openai-api-key-here

# Настройки GigaChat (обязательно для assistant_giga)
GIGACHAT_AUTH_KEY=your-basic-auth-token-here
GIGACHAT_RQUID=your-request-uid-here
```

### Получение API-ключей

#### OpenAI

1. Откройте <https://platform.openai.com/api-keys>
2. Создайте новый API-ключ
3. Скопируйте и вставьте в `.env`

#### GigaChat

1. Зарегистрируйтесь на <https://developers.sber.ru/gigachat>
2. Получите OAuth-учётку
3. Скопируйте `AUTH_KEY` и `RQUID` в `.env`

---

## 🚀 Использование

### Ассистент на OpenAI

```bash
# Активировать окружение
.\venv_py312\Scripts\Activate.ps1

# Перейти к OpenAI-ассистенту
cd assistant_api

# Запуск
python app.py
```

### Ассистент на GigaChat

```bash
# Активировать окружение
.\venv_py312\Scripts\Activate.ps1

# Перейти к GigaChat-ассистенту
cd assistant_giga

# Запуск
python app.py
```

### Оценка качества (только OpenAI)

```bash
cd assistant_api
python evaluate_ragas.py
```

### HTTP API и n8n

RAG Assistant (OpenAI) можно вызывать по HTTP и из n8n:

```bash
# Запуск API
cd assistant_api
python -m uvicorn api_server:app --host 0.0.0.0 --port 8000

# Проверка
curl -X POST http://localhost:8000/query -H "Content-Type: application/json" -d "{\"query\": \"Что такое RAG?\"}"
```

- Импорт workflow: `n8n/workflow-rag-query.json`
- n8n в Docker: `docker compose -f docker-compose.n8n.yml up -d`
- Подробно: [N8N_INTEGRATION.md](N8N_INTEGRATION.md)

### Команды в консоли

После запуска доступны команды:

| Команда | Описание |
| ------- | -------- |
| `exit`, `quit`, `q` | Выйти из приложения |
| `stats` | Показать статистику |
| `clear` | Очистить кеш (с подтверждением) |

### Пример сессии

```text
╔══════════════════════════════════════════════════════════╗
║         RAG Ассистент (API Mode)                        ║
║  Retrieval-Augmented Generation через OpenAI API        ║
╚══════════════════════════════════════════════════════════╝

💭 Ваш вопрос: Что такое RAG?

────────────────────────────────────────────────────────────
📝 Вопрос: Что такое RAG?
────────────────────────────────────────────────────────────
🌐 Источник: OpenAI API (gpt-4o-mini)
   Использовано документов: 3

💬 Ответ:
RAG (Retrieval-Augmented Generation) — это подход, который
комбинирует извлечение информации из базы знаний с генерацией
текста языковыми моделями. RAG-системы сначала находят релевантные
документы, затем используют их как контекст для генерации ответа...

📚 Использованный контекст:
   1. RAG (Retrieval-Augmented Generation) — это подход...
────────────────────────────────────────────────────────────
```

---

## 📁 Структура проекта

```text
rag-assistant/
│
├── 📄 README.md                    # этот файл
├── 📄 LICENSE                      # лицензия MIT
├── 📄 CONTRIBUTING.md              # как внести вклад
├── 📄 SETUP_COMPLETE.md            # лог установки
├── 📄 requirements.txt             # Python-зависимости
├── 📄 env.example                  # шаблон переменных окружения
├── 📄 .gitignore                   # правила git-ignore
├── 🔧 activate.ps1                 # скрипт активации (PowerShell)
├── 🔧 activate.bat                 # скрипт активации (CMD)
├── 🐳 docker-compose.n8n.yml       # n8n для автоматизации
├── 📄 N8N_INTEGRATION.md           # n8n и HTTP API
├── 📁 n8n/                         # n8n workflow'ы
│   └── workflow-rag-query.json     # webhook для RAG-запросов
│
├── 🔵 assistant_api/               # реализация на OpenAI
│   ├── 📄 OPENAI_INFO.md           # подробная документация
│   ├── 🐍 app.py                   # главное консольное приложение
│   ├── 🐍 api_server.py            # HTTP API (FastAPI) для n8n
│   ├── 🐍 rag_pipeline.py          # оркестрация RAG
│   ├── 🐍 vector_store.py          # ChromaDB + OpenAI эмбеддинги
│   ├── 🐍 cache.py                 # SQLite-кеш
│   ├── 🐍 evaluate_ragas.py        # оценка качества
│   └── 📁 data/
│       └── 📄 docs.txt             # база знаний
│
└── 🟢 assistant_giga/              # реализация на GigaChat
    ├── 📄 GIGACHAT_INFO.md         # подробная документация
    ├── 🐍 app.py                   # главное консольное приложение
    ├── 🐍 rag_pipeline.py          # оркестрация RAG
    ├── 🐍 vector_store.py          # ChromaDB + GigaChat эмбеддинги
    ├── 🐍 cache.py                 # SQLite-кеш
    ├── 🐍 gigachat_client.py       # клиент GigaChat API
    └── 📁 data/
        └── 📄 docs.txt             # база знаний
```

---

## 📚 Документация

### Основные документы

- **[SETUP_COMPLETE.md](SETUP_COMPLETE.md)** — полный гайд по установке
- **[N8N_INTEGRATION.md](N8N_INTEGRATION.md)** — HTTP API и n8n workflow
- **[OPENAI_INFO.md](assistant_api/OPENAI_INFO.md)** — детали реализации на OpenAI
- **[GIGACHAT_INFO.md](assistant_giga/GIGACHAT_INFO.md)** — детали реализации на GigaChat
- **[CONTRIBUTING.md](CONTRIBUTING.md)** — как внести вклад

### Темы в базе знаний

Встроенная база знаний охватывает:

- Основы машинного обучения
- Нейросети и глубокое обучение
- NLP и трансформеры
- Word Embeddings
- RAG-системы
- Векторные базы данных
- Prompt Engineering
- Fine-tuning
- Метрики качества LLM
- Стратегии кеширования в AI

---

## ⚡ Производительность

### Замеры

| Операция | Время | Стоимость (OpenAI) |
| -------- | ----- | ------------------ |
| Первый запрос | 2–5 сек | ~$0.001 |
| Из кеша | <100 мс | $0 |
| Чанкинг документов | ~1 сек | ~$0.0006 |
| Один эмбеддинг | ~0.5 сек | ~$0.00001 |

### Советы по оптимизации

1. **Используйте кеш** — повторные запросы мгновенные
2. **Оптимизируйте чанки** — баланс размера и релевантности
3. **Ограничьте `max_tokens`** — 500 достаточно для большинства ответов
4. **Используйте `gpt-4o-mini`** — в 60 раз дешевле GPT-4

---

## 🐛 Решение проблем

### Частые вопросы

#### «OPENAI_API_KEY not set»

**Решение:** создайте файл `.env` со своим API-ключом.

#### «ModuleNotFoundError»

**Решение:** активируйте виртуальное окружение:

```bash
.\venv_py312\Scripts\Activate.ps1
```

#### GigaChat «402 Payment Required»

**Решение:** это ожидаемое поведение для Embeddings API. Система использует fallback.

#### Медленные ответы

**Решение:**

- Используйте кеш (проверить через команду `stats`)
- Уменьшите `top_k` в поиске
- Уменьшите `max_tokens` при генерации

### Куда обратиться

- 📖 Проверьте файлы документации
- 🐛 Откройте issue на GitHub
- 💬 Задайте вопрос в Discussions

---

## 🤝 Вклад в проект

Контрибьюции приветствуются! Подробности — в [CONTRIBUTING.md](CONTRIBUTING.md).

### Быстрый старт для контрибьюторов

```bash
# Форк и клонирование
git clone https://github.com/Edwards359/rag-assistant.git

# Создать feature-ветку
git checkout -b feature/amazing-feature

# Внести изменения и протестировать

# Коммит и push
git commit -m 'Add amazing feature'
git push origin feature/amazing-feature

# Открыть Pull Request
```

---

## 📄 Лицензия

Проект распространяется по лицензии MIT. Детали — в файле [LICENSE](LICENSE).

---

## 🙏 Благодарности

### Технологии

- **[OpenAI](https://openai.com/)** — GPT-4 и API эмбеддингов
- **[GigaChat](https://developers.sber.ru/gigachat)** — русскоязычная LLM
- **[ChromaDB](https://www.trychroma.com/)** — векторная база
- **[LangChain](https://python.langchain.com/)** — фреймворк для LLM
- **[RAGAS](https://docs.ragas.io/)** — фреймворк оценки RAG

### Вдохновение

Проект создан для демонстрации лучших практик реализации RAG с разными LLM-бэкендами.

---

## 📊 Статус проекта

| Компонент | OpenAI | GigaChat |
| --------- | ------ | -------- |
| LLM API | ✅ | ✅ |
| Эмбеддинги | ✅ | ⚠️ Fallback |
| Векторный поиск | ✅ | ✅ |
| Кеш | ✅ | ✅ |
| Метрики качества | ✅ | ❌ |
| Документация | ✅ | ✅ |

**Легенда:** ✅ работает полностью | ⚠️ с ограничениями | ❌ недоступно

---

## 🔮 Roadmap

- [ ] Веб-интерфейс (Streamlit/Gradio)
- [ ] Поддержка разных форматов документов (PDF, DOCX)
- [ ] История диалога
- [ ] Многоязычная поддержка
- [ ] Развёртывание в Docker
- [ ] REST API эндпоинт
- [ ] Больше моделей эмбеддингов
- [ ] Гайд по production-развёртыванию

---

## 📞 Контакты

Ссылка на проект: [https://github.com/Edwards359/rag-assistant](https://github.com/Edwards359/rag-assistant)

---

<div align="center">

**Сделано с ❤️ на Python**

⭐ Поставьте звезду, если проект оказался полезен!

</div>
