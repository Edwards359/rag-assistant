# Скрипт активации виртуального окружения Python 3.11
# Использование: .\activate.ps1

Write-Host "🐍 Активация виртуального окружения Python 3.11..." -ForegroundColor Cyan
.\venv_py311\Scripts\Activate.ps1
Write-Host "✅ Виртуальное окружение активировано!" -ForegroundColor Green
Write-Host ""
Write-Host "📦 Доступные проекты:" -ForegroundColor Yellow
Write-Host "  1. assistant_api   - RAG с OpenAI API (cd assistant_api && python app.py)" -ForegroundColor White
Write-Host "  2. assistant_giga  - RAG с GigaChat    (cd assistant_giga && python app.py)" -ForegroundColor White
Write-Host ""
Write-Host "🧪 Оценка качества:" -ForegroundColor Yellow
Write-Host "  cd assistant_api && python evaluate_ragas.py" -ForegroundColor White
Write-Host ""
