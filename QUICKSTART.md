# ⚡ Quick Start Guide

Get started with RAG Assistant in 5 minutes!

---

## 📋 Prerequisites

- Python 3.11+
- Git
- OpenAI API Key OR GigaChat credentials

---

## 🚀 Installation (3 minutes)

### 1. Clone & Setup

```bash
# Clone repository
git clone https://github.com/yourusername/rag-assistant.git
cd rag-assistant

# Create virtual environment
py -3.11 -m venv venv_py311

# Activate (Windows PowerShell)
.\venv_py311\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure API Keys

```bash
# Copy template
copy env.example .env

# Edit .env with your API keys
notepad .env
```

Add your keys:
```env
OPENAI_API_KEY=sk-your-key-here
GIGACHAT_AUTH_KEY=your-key-here
GIGACHAT_RQUID=your-rquid-here
```

---

## 🎯 Run (1 minute)

### Option A: OpenAI Assistant

```bash
cd assistant_api
python app.py
```

### Option B: GigaChat Assistant

```bash
cd assistant_giga
python app.py
```

---

## 💬 Try It!

Once running, ask questions:

```
💭 Ваш вопрос: Что такое RAG?

────────────────────────────────────────────────────────────
📝 Вопрос: Что такое RAG?
🌐 Источник: OpenAI API (gpt-4o-mini)

💬 Ответ:
RAG (Retrieval-Augmented Generation) - это подход, который 
комбинирует извлечение информации из базы знаний с генерацией 
текста языковыми моделями...
────────────────────────────────────────────────────────────
```

### Available Commands

- Type your question and press Enter
- `exit` - quit application
- `stats` - show system statistics
- `clear` - clear cache

---

## 📊 Evaluate Quality (Optional)

For OpenAI implementation:

```bash
cd assistant_api
python evaluate_ragas.py
```

---

## 🎉 That's It!

You're ready to use RAG Assistant!

**Next Steps:**
- Read [EXAMPLES.md](EXAMPLES.md) for more usage examples
- Check [OPENAI_INFO.md](assistant_api/OPENAI_INFO.md) for OpenAI details
- Check [GIGACHAT_INFO.md](assistant_giga/GIGACHAT_INFO.md) for GigaChat details

---

## 🐛 Troubleshooting

**Problem:** `ModuleNotFoundError`  
**Solution:** Make sure virtual environment is activated

**Problem:** `OPENAI_API_KEY not set`  
**Solution:** Check `.env` file exists and contains your key

**Problem:** Slow responses  
**Solution:** Repeated queries use cache and are instant!

---

## 💡 Tips

1. **Use cache** - Same questions return instantly
2. **Check stats** - Type `stats` to see cache hits
3. **Be specific** - Clear questions get better answers

---

**Ready to explore? Let's go!** 🚀
