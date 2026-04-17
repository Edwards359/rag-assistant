# 🚀 Команды для публикации на GitHub

## Готовые команды для копирования

### Шаг 1: Создайте репозиторий на GitHub

1. Перейдите на: https://github.com/new
2. Repository name: `rag-assistant`
3. Description: `Dual RAG implementation with OpenAI and GigaChat backends`
4. Выберите Public или Private
5. ⚠️ НЕ добавляйте README, .gitignore, License (они уже есть!)
6. Нажмите "Create repository"

---

### Шаг 2: Выполните эти команды

**Скопируйте и выполните в PowerShell:**

```powershell
# Подключите remote репозиторий
git remote add origin https://github.com/Edwards359/rag-assistant.git

# Переименуйте ветку в main
git branch -M main

# Отправьте код на GitHub
git push -u origin main
```

---

### Альтернативно (если используете SSH):

```bash
git remote add origin git@github.com:Edwards359/rag-assistant.git
git branch -M main
git push -u origin main
```

---

## ✅ После успешного push:

Ваш проект будет доступен по адресу:
**https://github.com/Edwards359/rag-assistant**

---

## 🎨 Настройте репозиторий:

### 1. About (правая панель на GitHub):

- **Description:** `Dual RAG implementation with OpenAI and GigaChat backends`
- **Topics:** добавьте теги:
  ```
  rag, llm, openai, gpt-4, gigachat, chromadb, langchain, ragas, 
  python, machine-learning, nlp, vector-database, semantic-search, ai
  ```

### 2. Settings → Features:

- ✅ Issues (для баг-репортов)
- ✅ Discussions (опционально, для Q&A)

### 3. Создайте Release (опционально):

- Releases → Create a new release
- Tag: `v1.0.0`
- Title: `v1.0.0 - Initial Release`
- Description: используйте текст из CHANGELOG.md

---

## 📊 Что будет на GitHub:

- 35 файлов
- 6342 строк кода
- Полная документация
- Два рабочих проекта
- MIT License
- .gitignore настроен
- README с badges

---

## 🎉 Готово!

После выполнения команд ваш проект будет опубликован!

**URL:** https://github.com/Edwards359/rag-assistant
