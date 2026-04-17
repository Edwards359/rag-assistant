# Как выложить README в профиль GitHub (Edwards359/Edwards359)

## Профильный README

В репозитории **Edwards359/Edwards359** файл `README.md` показывается на главной странице вашего профиля:  
https://github.com/Edwards359

---

## Шаги

### 1. Создать репозиторий

1. Откройте: https://github.com/new  
2. **Repository name:** `Edwards359` (обязательно как ваш логин)  
3. **Description:** по желанию, например: `Profile`  
4. Выберите **Public**  
5. **НЕ** ставьте: Add a README, .gitignore, License  
6. Нажмите **Create repository**

### 2. Добавить README.md

**Вариант А — через веб-интерфейс**

1. В пустом репо нажмите **Add a README file** (или «create a new file»).  
2. Имя файла: `README.md`  
3. Вставьте содержимое из `PROFILE_README_Edwards359.md`  
4. **Commit** — «Commit new file» / «Create README».

**Вариант Б — через Git (если репо уже есть)**

```bash
# Клонировать
git clone https://github.com/Edwards359/Edwards359.git
cd Edwards359

# Скопировать README из нашего проекта
copy "C:\MyProjectsCursor\Per08\PROFILE_README_Edwards359.md" README.md

# Закоммитить и отправить
git add README.md
git commit -m "Add profile README"
git push
```

### 3. Проверить

Откройте https://github.com/Edwards359 — блок с `README.md` должен отображаться над списком репозиториев.

---

## Файлы

| Файл | Назначение |
|------|------------|
| `PROFILE_README_Edwards359.md` | Исходник README для профиля — копировать в `Edwards359/Edwards359` как `README.md` |
| `GITHUB_PROFILE_SETUP.md` | Эта инструкция |

---

## Если картинки GitHub Stats не отображаются

Сервис [github-readme-stats](https://github.com/anuraghazra/github-readme-stats) иногда грузится с задержкой.  
Если не нужны — удалите в `README.md` весь блок:

```markdown
## 📊 GitHub

<div align="center">
...
</div>
```

Останется текст, ссылки и таблицы — профиль будет работать и без статистики.

---

## Доработки под себя

В `PROFILE_README_Edwards359.md` можно:

- поменять текст в «Обо мне»;
- добавить ссылки (Telegram, email, LinkedIn и т.п.) в раздел «Связь»;
- добавить новые проекты в «Проекты»;
- обновить список технологий.

После правок снова закоммитьте и сделайте `git push` в репозиторий **Edwards359/Edwards359**.
