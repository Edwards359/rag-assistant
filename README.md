# 🤖 RAG Assistant - Dual Implementation

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11.9-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991.svg)
![GigaChat](https://img.shields.io/badge/GigaChat-Sber-orange.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success.svg)

**Two production-ready RAG (Retrieval-Augmented Generation) assistants with different LLM backends**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Documentation](#-documentation) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [About](#-about-the-project)
- [Architecture](#-architecture)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Documentation](#-documentation)
- [Performance](#-performance)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

---

## 🎯 About The Project

This project demonstrates two complete RAG (Retrieval-Augmented Generation) implementations using different Large Language Model backends:

### 🔵 OpenAI Implementation (`assistant_api`)
- **LLM:** GPT-4o-mini
- **Embeddings:** text-embedding-3-small
- **Quality Evaluation:** RAGAS metrics
- **Status:** ✅ Fully functional

### 🟢 GigaChat Implementation (`assistant_giga`)
- **LLM:** GigaChat by Sber
- **Embeddings:** GigaChat Embeddings API (with fallback)
- **Status:** ✅ Functional with limitations

Both implementations share:
- **Vector Database:** ChromaDB
- **Caching:** SQLite
- **Smart Chunking:** Semantic text splitting with overlap
- **Console Interface:** Interactive CLI

---

## 🏗️ Architecture

```
┌─────────────┐
│ User Query  │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│  Cache Check    │ ◄─── SQLite DB
│  (SHA-256 hash) │
└────────┬────────┘
         │
    ┌────┴────┐
    │  Hit?   │
    └─┬────┬──┘
  Yes │    │ No
      │    ▼
      │  ┌──────────────────┐
      │  │ Vector Search    │ ◄─── ChromaDB
      │  │ (Top-K=3)        │
      │  └────────┬─────────┘
      │           │
      │           ▼
      │  ┌──────────────────┐
      │  │ Context Building │
      │  │ (Prompt + Docs)  │
      │  └────────┬─────────┘
      │           │
      │           ▼
      │  ┌──────────────────┐
      │  │ LLM Generation   │ ◄─── OpenAI / GigaChat
      │  │ (Temperature=0.3)│
      │  └────────┬─────────┘
      │           │
      │           ▼
      │  ┌──────────────────┐
      │  │ Cache Storage    │
      │  └────────┬─────────┘
      │           │
      └───────────┘
              │
              ▼
      ┌─────────────┐
      │   Response  │
      └─────────────┘
```

---

## ✨ Features

### Core Functionality

- **✅ Semantic Search** - Find relevant context using vector embeddings
- **✅ Smart Caching** - Instant responses for repeated queries (<100ms)
- **✅ Intelligent Chunking** - Semantic text splitting with overlap
- **✅ Dual LLM Support** - Choose between OpenAI and GigaChat
- **✅ Quality Metrics** - RAGAS evaluation for OpenAI implementation
- **✅ Console Interface** - User-friendly CLI with commands
- **✅ Statistics** - Track cache hits, document counts, performance

### Advanced Features

- **Context Preservation** - Overlap between chunks maintains coherence
- **Normalized Queries** - Case-insensitive, whitespace-normalized caching
- **Automatic Retry** - OAuth token refresh for GigaChat
- **Fallback Embeddings** - Hash-based vectors when API unavailable
- **Detailed Logging** - Track every step of the pipeline

---

## 🛠️ Tech Stack

### Core Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.11.9 | Runtime environment |
| **OpenAI API** | 2.15.0 | LLM & Embeddings (assistant_api) |
| **GigaChat API** | - | Russian LLM (assistant_giga) |
| **ChromaDB** | 1.4.0 | Vector database |
| **LangChain** | 1.2.3 | LLM framework |
| **RAGAS** | 0.4.2 | RAG quality evaluation |

### Supporting Libraries

```python
sentence-transformers  # 5.2.0  - Transformer models
numpy                  # 2.4.1  - Numerical operations
pandas                 # 2.3.3  - Data manipulation
tiktoken              # 0.12.0 - Token counting
python-dotenv         # 1.2.1  - Environment management
```

---

## 📥 Installation

### Prerequisites

- **Python 3.11+** (tested on 3.11.9)
- **Git**
- **OpenAI API Key** (for assistant_api)
- **GigaChat Credentials** (for assistant_giga)

### Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/rag-assistant.git
cd rag-assistant

# Create virtual environment
py -3.11 -m venv venv_py311

# Activate (Windows PowerShell)
.\venv_py311\Scripts\Activate.ps1

# Activate (Windows CMD)
.\venv_py311\Scripts\activate.bat

# Activate (Linux/Mac)
source venv_py311/bin/activate

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
copy env.example .env
# Edit .env with your API keys
```

### Alternative: Using Activation Scripts

```bash
# Windows PowerShell
.\activate.ps1

# Windows CMD
activate.bat
```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# OpenAI Configuration (required for assistant_api)
OPENAI_API_KEY=sk-your-openai-api-key-here

# GigaChat Configuration (required for assistant_giga)
GIGACHAT_AUTH_KEY=your-basic-auth-token-here
GIGACHAT_RQUID=your-request-uid-here
```

### Getting API Keys

#### OpenAI
1. Visit https://platform.openai.com/api-keys
2. Create a new API key
3. Copy and paste into `.env`

#### GigaChat
1. Register at https://developers.sber.ru/gigachat
2. Get your OAuth credentials
3. Copy AUTH_KEY and RQUID into `.env`

---

## 🚀 Usage

### OpenAI Assistant

```bash
# Activate environment
.\venv_py311\Scripts\Activate.ps1

# Navigate to OpenAI assistant
cd assistant_api

# Run
python app.py
```

### GigaChat Assistant

```bash
# Activate environment
.\venv_py311\Scripts\Activate.ps1

# Navigate to GigaChat assistant
cd assistant_giga

# Run
python app.py
```

### Quality Evaluation (OpenAI only)

```bash
cd assistant_api
python evaluate_ragas.py
```

### Console Commands

Once running, use these commands:

| Command | Description |
|---------|-------------|
| `exit`, `quit`, `q` | Exit the application |
| `stats` | Show system statistics |
| `clear` | Clear the cache (with confirmation) |

### Example Session

```
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
RAG (Retrieval-Augmented Generation) - это подход, который 
комбинирует извлечение информации из базы знаний с генерацией 
текста языковыми моделями. RAG системы сначала находят релевантные 
документы, затем используют их как контекст для генерации ответа...

📚 Использованный контекст:
   1. RAG (Retrieval-Augmented Generation) - это подход...
────────────────────────────────────────────────────────────
```

---

## 📁 Project Structure

```
rag-assistant/
│
├── 📄 README.md                    # This file
├── 📄 LICENSE                      # MIT License
├── 📄 CONTRIBUTING.md              # Contribution guidelines
├── 📄 SETUP_COMPLETE.md            # Installation log
├── 📄 requirements.txt             # Python dependencies
├── 📄 env.example                  # Environment template
├── 📄 .gitignore                   # Git ignore rules
├── 🔧 activate.ps1                 # PowerShell activation script
├── 🔧 activate.bat                 # CMD activation script
│
├── 🔵 assistant_api/               # OpenAI Implementation
│   ├── 📄 OPENAI_INFO.md          # Detailed documentation
│   ├── 🐍 app.py                  # Main console application
│   ├── 🐍 rag_pipeline.py         # RAG orchestration
│   ├── 🐍 vector_store.py         # ChromaDB + OpenAI embeddings
│   ├── 🐍 cache.py                # SQLite caching
│   ├── 🐍 evaluate_ragas.py       # Quality evaluation
│   └── 📁 data/
│       └── 📄 docs.txt            # Knowledge base
│
└── 🟢 assistant_giga/              # GigaChat Implementation
    ├── 📄 GIGACHAT_INFO.md        # Detailed documentation
    ├── 🐍 app.py                  # Main console application
    ├── 🐍 rag_pipeline.py         # RAG orchestration
    ├── 🐍 vector_store.py         # ChromaDB + GigaChat embeddings
    ├── 🐍 cache.py                # SQLite caching
    ├── 🐍 gigachat_client.py      # GigaChat API client
    └── 📁 data/
        └── 📄 docs.txt            # Knowledge base
```

---

## 📚 Documentation

### Main Documents

- **[SETUP_COMPLETE.md](SETUP_COMPLETE.md)** - Complete installation guide
- **[OPENAI_INFO.md](assistant_api/OPENAI_INFO.md)** - OpenAI implementation details
- **[GIGACHAT_INFO.md](assistant_giga/GIGACHAT_INFO.md)** - GigaChat implementation details
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute

### Knowledge Base Topics

The included knowledge base covers:
- Machine Learning fundamentals
- Neural Networks and Deep Learning
- NLP and Transformers
- Word Embeddings
- RAG Systems
- Vector Databases
- Prompt Engineering
- Fine-tuning
- LLM Quality Metrics
- AI Caching strategies

---

## ⚡ Performance

### Benchmarks

| Operation | Time | Cost (OpenAI) |
|-----------|------|---------------|
| First query | 2-5 sec | ~$0.001 |
| Cached query | <100ms | $0 |
| Document chunking | ~1 sec | ~$0.0006 |
| Single embedding | ~0.5 sec | ~$0.00001 |

### Optimization Tips

1. **Use Cache** - Repeated queries are instant
2. **Optimize Chunks** - Balance size vs. relevance
3. **Limit max_tokens** - 500 is sufficient for most answers
4. **Use gpt-4o-mini** - 60x cheaper than GPT-4

---

## 🐛 Troubleshooting

### Common Issues

#### "OPENAI_API_KEY not set"
**Solution:** Create `.env` file with your API key

#### "ModuleNotFoundError"
**Solution:** Activate virtual environment:
```bash
.\venv_py311\Scripts\Activate.ps1
```

#### GigaChat "402 Payment Required"
**Solution:** This is normal for Embeddings API. System uses fallback.

#### Slow responses
**Solution:** 
- Use cache (check with `stats` command)
- Reduce `top_k` in search
- Decrease `max_tokens` in generation

### Getting Help

- 📖 Check documentation files
- 🐛 Open an issue on GitHub
- 💬 Ask in discussions

---

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Start for Contributors

```bash
# Fork and clone
git clone https://github.com/yourusername/rag-assistant.git

# Create feature branch
git checkout -b feature/amazing-feature

# Make changes and test

# Commit and push
git commit -m 'Add amazing feature'
git push origin feature/amazing-feature

# Open Pull Request
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

### Technologies

- **[OpenAI](https://openai.com/)** - GPT-4 and embeddings API
- **[GigaChat](https://developers.sber.ru/gigachat)** - Russian language model
- **[ChromaDB](https://www.trychroma.com/)** - Vector database
- **[LangChain](https://python.langchain.com/)** - LLM framework
- **[RAGAS](https://docs.ragas.io/)** - RAG evaluation framework

### Inspiration

This project was built to demonstrate best practices in RAG implementation with different LLM backends.

---

## 📊 Project Status

| Component | OpenAI | GigaChat |
|-----------|--------|----------|
| LLM API | ✅ | ✅ |
| Embeddings | ✅ | ⚠️ Fallback |
| Vector Search | ✅ | ✅ |
| Caching | ✅ | ✅ |
| Quality Metrics | ✅ | ❌ |
| Documentation | ✅ | ✅ |

**Legend:** ✅ Fully Functional | ⚠️ Limited | ❌ Not Available

---

## 🔮 Roadmap

- [ ] Add web interface (Streamlit/Gradio)
- [ ] Support for multiple document formats (PDF, DOCX)
- [ ] Conversation history
- [ ] Multi-language support
- [ ] Docker deployment
- [ ] REST API endpoint
- [ ] More embedding models
- [ ] Production deployment guide

---

## 📞 Contact

Project Link: [https://github.com/yourusername/rag-assistant](https://github.com/yourusername/rag-assistant)

---

<div align="center">

**Made with ❤️ and Python**

⭐ Star this repo if you find it useful!

</div>
