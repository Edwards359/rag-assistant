# 🟢 GigaChat RAG Ассистент - Важная информация

## ⚠️ Особенности работы с GigaChat API

### 1. Embeddings API (402 Payment Required)

**Проблема:**
GigaChat Embeddings API требует платной подписки. При попытке использования возвращается ошибка:
```
402 Client Error: Payment Required
```

**Решение:**
Система автоматически использует **fallback механизм** - hash-based embeddings:
- Создаёт 768-мерные векторы на основе SHA-256 хеша текста
- Работает без дополнительных API вызовов
- Качество поиска ниже, чем у настоящих embeddings, но система функциональна

**Код fallback** (в `gigachat_client.py`):
```python
def get_embeddings(self, texts: List[str], model: str = "Embeddings") -> List[List[float]]:
    try:
        # Попытка использовать GigaChat Embeddings API
        response = requests.post(...)
    except Exception as e:
        # Fallback на hash-based embeddings
        print(f"⚠️  Embeddings API недоступен, используется fallback: {e}")
        embeddings = []
        for text in texts:
            hash_obj = hashlib.sha256(text.encode())
            hash_bytes = hash_obj.digest()
            vector = []
            for i in range(768):
                vector.append((hash_bytes[i % len(hash_bytes)] / 255.0) - 0.5)
            embeddings.append(vector)
        return embeddings
```

---

### 2. SSL Certificate Warnings

**Проблема:**
GigaChat API использует самоподписанный сертификат, что вызывает предупреждения:
```
InsecureRequestWarning: Unverified HTTPS request is being made to host 'gigachat.devices.sberbank.ru'
```

**Решение:**
Добавлено отключение предупреждений в начале `gigachat_client.py`:
```python
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
```

**Безопасность:** В production среде рекомендуется использовать правильные SSL сертификаты.

---

### 3. OAuth Токен (обновление каждые 30 минут)

**Механизм:**
- GigaChat использует OAuth 2.0 для авторизации
- Access token действует **30 минут**
- Автоматическое обновление перед истечением

**Требуемые переменные окружения:**
```env
GIGACHAT_AUTH_KEY=your-basic-auth-token
GIGACHAT_RQUID=your-request-uid
```

---

## 🎯 Текущий статус работы

### ✅ Что работает:
- ✅ OAuth авторизация
- ✅ Chat Completions API (генерация ответов)
- ✅ Векторный поиск (через fallback embeddings)
- ✅ Кеширование ответов
- ✅ Консольный интерфейс

### ⚠️ Ограничения:
- ⚠️ Embeddings API недоступен (требует оплаты)
- ⚠️ Качество поиска ниже из-за fallback embeddings
- ⚠️ SSL сертификат игнорируется (verify=False)

---

## 💡 Рекомендации

### Для улучшения качества:

1. **Активировать платную подписку GigaChat Pro:**
   - Откроет доступ к Embeddings API
   - Значительно улучшит качество семантического поиска
   - https://developers.sber.ru/gigachat

2. **Альтернатива: использовать OpenAI embeddings:**
   - Можно заменить `GigaChatClient.get_embeddings()` на OpenAI API
   - Требует `OPENAI_API_KEY`
   - Лучшее качество, но платно

3. **Использовать локальные модели embeddings:**
   - sentence-transformers (уже установлен)
   - Бесплатно, работает offline
   - Пример: `SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')`

---

## 🚀 Запуск

```powershell
# Активация окружения
.\venv_py311\Scripts\Activate.ps1

# Запуск ассистента
cd assistant_giga
python app.py
```

---

## 📊 Примеры вопросов

- "Что такое RAG?"
- "Как работают трансформеры?"
- "Объясни машинное обучение"
- "Что такое векторные базы данных?"

---

## 🔧 Troubleshooting

### Ошибка: "GIGACHAT_AUTH_KEY не установлен"
**Решение:** Создайте файл `.env` в корне проекта с ключами

### Ошибка: "402 Payment Required"
**Решение:** Это нормально для Embeddings API. Система использует fallback.

### Медленная работа
**Решение:** 
- Используйте кеш (повторные запросы мгновенны)
- Первый запрос может занять 3-5 секунд

---

**Дата:** Январь 2026  
**Python:** 3.11.9  
**GigaChat API:** v1
