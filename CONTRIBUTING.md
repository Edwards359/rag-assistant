# Contributing to RAG Assistant

Thank you for your interest in contributing to the RAG Assistant project! 🎉

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- A clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Your environment (Python version, OS, etc.)

### Suggesting Enhancements

We welcome suggestions! Please open an issue describing:
- The enhancement you'd like to see
- Why it would be useful
- Any implementation ideas you have

### Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test your changes thoroughly
5. Commit with clear messages (`git commit -m 'Add amazing feature'`)
6. Push to your branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines
- Add docstrings to functions and classes
- Keep functions focused and small
- Write meaningful variable names

### Testing

- Test both OpenAI and GigaChat implementations
- Verify cache functionality
- Check edge cases

### Documentation

- Update README.md if needed
- Add comments for complex logic
- Update relevant info files (OPENAI_INFO.md, GIGACHAT_INFO.md)

## Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/rag-assistant.git
cd rag-assistant

# Create virtual environment
py -3.11 -m venv venv_py311
.\venv_py311\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment variables
copy env.example .env
# Edit .env with your API keys
```

## Questions?

Feel free to open an issue for any questions!

Thank you for contributing! 🚀
