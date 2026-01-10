# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-01-11

### Added
- Initial release of RAG Assistant with dual implementation
- OpenAI implementation (assistant_api) with GPT-4o-mini
- GigaChat implementation (assistant_giga) with Sber LLM
- ChromaDB vector database integration
- SQLite caching system
- RAGAS quality evaluation for OpenAI
- Smart chunking with semantic overlap
- Console interface with interactive commands
- Comprehensive documentation
- Activation scripts for Windows (PowerShell and CMD)
- Environment variable templates
- MIT License
- Contributing guidelines

### Features - OpenAI Implementation
- GPT-4o-mini for text generation
- text-embedding-3-small for vector embeddings
- RAGAS quality metrics (Faithfulness, Context Precision)
- Full API integration with error handling
- Cost optimization with efficient token usage

### Features - GigaChat Implementation
- GigaChat API for text generation
- GigaChat Embeddings with automatic fallback
- OAuth 2.0 token management with auto-refresh
- SSL certificate handling
- Russian language optimization

### Features - Common
- Vector search with ChromaDB (cosine similarity)
- SQLite caching with SHA-256 query hashing
- Smart text chunking (500 chars, 100 char overlap)
- Console interface with stats and clear commands
- Detailed logging and error messages
- Environment-based configuration

### Documentation
- Main README with project overview
- GitHub-ready README with badges and structure
- SETUP_COMPLETE.md with installation log
- OPENAI_INFO.md with OpenAI-specific details
- GIGACHAT_INFO.md with GigaChat-specific details
- CONTRIBUTING.md with contribution guidelines
- CHANGELOG.md (this file)

### Technical Details
- Python 3.11.9 requirement
- 150+ dependencies installed
- Virtual environment support
- Cross-platform compatibility (Windows focus)

## [Unreleased]

### Planned
- Web interface (Streamlit/Gradio)
- Multiple document format support (PDF, DOCX)
- Conversation history
- Multi-language support
- Docker deployment
- REST API endpoint
- Additional embedding models
- Production deployment guide

---

## Version History

### [1.0.0] - 2026-01-11
- Initial public release

---

**Note:** This is the first public release. All features are production-ready and tested.
