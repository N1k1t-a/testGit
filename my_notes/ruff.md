# Ruff — полный гайд

## Что такое Ruff

Ruff — линтер и форматтер для Python, написанный на Rust. Заменяет сразу несколько инструментов:

| Старый инструмент | Что делал               |
|-------------------|-------------------------|
| flake8            | проверка стиля          |
| black             | форматирование          |
| isort             | сортировка импортов     |
| pyupgrade         | обновление синтаксиса   |
| flake8-bugbear    | поиск багов             |

Главное преимущество — скорость (в 10-100 раз быстрее аналогов) и то, что всё в одном инструменте.

---

## Установка

```bash
pip install ruff
```

Проверить установку:
```bash
ruff --version
```

---

## Команды в консоли

### Проверка (lint)

```bash
# Проверить весь проект
ruff check .

# Проверить конкретный файл
ruff check main.py

# Проверить папку
ruff check code_otus/

# Показать подробное описание каждой ошибки
ruff check . --show-source

# Показать статистику по правилам
ruff check . --statistics
```

### Автоисправление

```bash
# Исправить всё что можно автоматически
ruff check . --fix

# Исправить конкретный файл
ruff check main.py --fix

# Показать что изменится, но не применять
ruff check . --fix --diff
```

### Форматирование

```bash
# Отформатировать весь проект
ruff format .

# Отформатировать файл
ruff format main.py

# Показать что изменится, но не применять
ruff format . --diff

# Проверить — отформатировано ли (без изменений, только статус)
ruff format . --check
```

### Информация о правилах

```bash
# Объяснение конкретного правила
ruff rule E501

# Список всех доступных правил
ruff rule --all
```

---

## Конфигурация — pyproject.toml

Файл `pyproject.toml` кладётся в корень проекта. Ruff работает и без него (с настройками по умолчанию), но с ним можно всё тонко настроить.

```toml
[tool.ruff]
# Длина строки
line-length = 120

# Версия Python
target-version = "py312"

# Папки которые игнорировать
exclude = [
    ".venv",
    "venv",
    ".git",
    "__pycache__",
    "migrations",   # если Django
]

[tool.ruff.lint]
# Группы правил которые включить
select = [
    "E",   # pycodestyle errors — базовые ошибки стиля
    "W",   # pycodestyle warnings — предупреждения стиля
    "F",   # pyflakes — неиспользуемые импорты, переменные
    "I",   # isort — порядок импортов
    "N",   # pep8-naming — правила именования
    "B",   # flake8-bugbear — потенциальные баги
    "C4",  # flake8-comprehensions — упрощение list/dict comprehension
    "UP",  # pyupgrade — использование нового синтаксиса Python
    "SIM", # flake8-simplify — упрощение кода
    "RUF", # ruff-specific — правила самого ruff
]

# Правила которые игнорировать
ignore = [
    "E501",   # line too long (если не хочешь контролировать длину)
    "RUF001", # кириллица в строках — важно для русских проектов
    "RUF003", # кириллица в комментариях
]

# Что можно автоматически исправлять
fixable = ["ALL"]
unfixable = []

# Игнорировать конкретные файлы
per-file-ignores = { "tests/**" = ["S101"] }  # в тестах разрешены assert

[tool.ruff.format]
quote-style = "double"          # двойные кавычки (как black)
indent-style = "space"          # отступы пробелами
skip-magic-trailing-comma = false
```

### Основные группы правил (select)

| Код  | Название              | Что проверяет                          |
|------|-----------------------|----------------------------------------|
| E    | pycodestyle errors    | пробелы, отступы, базовый стиль        |
| W    | pycodestyle warnings  | предупреждения стиля                   |
| F    | pyflakes              | неиспользуемые импорты и переменные    |
| I    | isort                 | порядок и группировка импортов         |
| N    | pep8-naming           | имена классов, функций, переменных     |
| B    | flake8-bugbear        | типичные баги и плохие практики        |
| C4   | flake8-comprehensions | [x for x in y] вместо list(...)        |
| UP   | pyupgrade             | f-строки, новый синтаксис typing       |
| SIM  | flake8-simplify       | упрощение if/else, with и т.д.         |
| S    | bandit                | безопасность (sql injection и т.д.)    |
| T20  | flake8-print          | запрет print() в продакшн коде         |
| RUF  | ruff-specific         | дополнительные правила от ruff         |

---

## Настройка в PyCharm

### Шаг 1 — установить плагин

```
Settings (Ctrl+Alt+S)
→ Plugins
→ Marketplace
→ поиск: "Ruff"
→ Install
→ Restart IDE
```

### Шаг 2 — настроить плагин

```
Settings → Tools → Ruff
```

#### Галочки — что включать

| Галочка | Включать? | Что делает |
|---|---|---|
| **Run ruff when the python file is saved** | ✅ ДА | Запускает проверку при каждом сохранении файла. Главная галочка — включи обязательно |
| **Exclude files outside of the project** | ✅ ДА | Появляется под предыдущей. Не проверяет чужие библиотеки из venv |
| **Run ruff when Reformat Code** | ✅ ДА | Ruff форматирует когда нажимаешь Ctrl+Alt+L |
| **Show Rule Code on inspection message** | ✅ ДА | Показывает код правила (E501, F401) в подсказках — удобно для поиска в документации |
| **Always use Global executable** | ❌ НЕТ | Использовать глобальный ruff вместо из venv проекта. Оставь выключенной — пусть использует ruff из твоего окружения |
| **Use ruff-lsp (Experimental)** | ❌ НЕТ | Устаревший экспериментальный режим. Не нужен |
| **Use `ruff server` for LSP functionality** | ✅ ДА | Современный режим — подсветка ошибок прямо в редакторе в реальном времени. Включи если хочешь видеть ошибки сразу, без сохранения |
| **Use ruff format (Experimental)** | ✅ ДА | Включает `ruff format` (форматтер). Включи — иначе ruff будет только линтить, но не форматировать |

#### Проблема "Ruff executable not found"

Если в полях написано "Ruff executable not found" — PyCharm не нашёл ruff автоматически.

Нажми **Auto-detect ruff** — PyCharm попробует найти сам.

Если не помогло — укажи путь вручную в поле **Project Specific → ruff executable**:
```
C:\Users\aboob\PycharmProjects\testGit\venv_win\Scripts\ruff.exe
```

Секция **Global** — путь к ruff для всех проектов сразу (если используешь один ruff глобально).
Секция **Project Specific** — путь к ruff конкретно для этого проекта (рекомендую использовать именно её).

#### Ruff config file

Поле внизу — путь к файлу конфигурации. Оставь пустым — ruff сам найдёт `pyproject.toml` в корне проекта.

### Шаг 3 — форматирование по Ctrl+Alt+L

Чтобы `Ctrl+Alt+L` (стандартный шорткат форматирования в PyCharm) использовал ruff:

```
Settings
→ Editor
→ Code Style
→ нажать шестерёнку ⚙️ рядом с "Python"
→ выбрать "Use Ruff formatter"
```

---

## Pre-commit хуки

Pre-commit — инструмент который запускает проверки **перед каждым git commit**.
Если ruff найдёт проблемы — коммит не пройдёт.

### Установка

```bash
pip install pre-commit
```

### Создать файл `.pre-commit-config.yaml` в корне проекта

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.9.0  # актуальную версию смотри на https://github.com/astral-sh/ruff-pre-commit
    hooks:
      - id: ruff          # линтер (проверка + исправление)
        args: [--fix]
      - id: ruff-format   # форматтер
```

### Установить хуки в git

```bash
pre-commit install
```

После этого при каждом `git commit` автоматически запустится ruff.

### Как это выглядит в работе

```
$ git commit -m "добавил фичу"

ruff....................................................................Failed
- hook id: ruff
- files were modified by hook

Fixed 3 errors.
```

Ruff исправил файлы — нужно их снова добавить в коммит:
```bash
git add .
git commit -m "добавил фичу"  # теперь пройдёт
```

### Запустить pre-commit вручную (без коммита)

```bash
# Проверить все файлы
pre-commit run --all-files

# Проверить только конкретный хук
pre-commit run ruff --all-files
```

### Обновить версии хуков

```bash
pre-commit autoupdate
```

---

## Игнорирование в коде

Иногда нужно отключить правило для конкретной строки:

```python
import os  # noqa: F401        — игнорировать конкретное правило
import sys  # noqa              — игнорировать все правила для строки

# ruff: noqa: E501              — игнорировать правило для всего файла (в начале файла)
```

---

## Типичные ошибки и что они значат

| Код  | Пример                          | Проблема                        |
|------|---------------------------------|---------------------------------|
| F401 | `import os` (не используется)   | неиспользуемый импорт           |
| F811 | повторное определение функции   | переопределение имени           |
| E501 | строка длиннее line-length      | слишком длинная строка          |
| I001 | импорты не отсортированы        | нарушен порядок импортов        |
| B006 | `def f(x=[]):`                  | мутабельный аргумент по умолчанию |
| UP007 | `Optional[str]`                | используй `str | None`          |
| SIM108 | длинный if/else               | можно заменить на тернарный     |

---

## Ruff vs Black — итог

Не используй их вместе — они конфликтуют.

| | Black | Ruff |
|---|---|---|
| Форматирование | ✅ | ✅ (совместим с Black) |
| Линтинг | ❌ | ✅ |
| Сортировка импортов | ❌ (нужен isort) | ✅ |
| Скорость | медленнее | быстрее в 10-100 раз |
| Настройка | минимальная | гибкая |

**Вывод:** Ruff делает всё то же что Black + даёт линтинг. Смысла использовать Black нет.

---

## Быстрая шпаргалка

```bash
ruff check .              # проверить проект
ruff check . --fix        # проверить и исправить
ruff format .             # отформатировать
ruff format . --check     # проверить форматирование (без изменений)
ruff rule F401            # объяснение правила
pre-commit run --all-files  # запустить все хуки вручную
```
