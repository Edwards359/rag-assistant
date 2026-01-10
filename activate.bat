@echo off
REM Скрипт активации виртуального окружения Python 3.11
REM Использование: activate.bat

echo 🐍 Активация виртуального окружения Python 3.11...
call .\venv_py311\Scripts\activate.bat
echo ✅ Виртуальное окружение активировано!
echo.
echo 📦 Доступные проекты:
echo   1. assistant_api   - RAG с OpenAI API (cd assistant_api ^&^& python app.py)
echo   2. assistant_giga  - RAG с GigaChat    (cd assistant_giga ^&^& python app.py)
echo.
echo 🧪 Оценка качества:
echo   cd assistant_api ^&^& python evaluate_ragas.py
echo.
