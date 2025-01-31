# Food tracker

**Food tracker** — это система учета питания и подсчета калорий. Приложение помогает пользователям отслеживать свои приемы пищи, анализировать потребление калорий и макронутриентов (белков, жиров и углеводов), а также контролировать прогресс в достижении своих целей.

## Основные функции
- Регистрация и авторизация пользователей.
- Добавление продуктов из справочника (с указанием калорийности, БЖУ).
- Ведение дневника питания с разбивкой на приемы пищи (завтрак, обед, ужин, перекус).
- Автоматический подсчет потребленных калорий и макронутриентов.
- Анализ данных в виде статистики и графиков.

## Запуск проекта для разработки

### Windows:
- `python -m venv venv` - создание виртуального окружения
- `venv\\Scripts\\activate` - активация виртуального окружения
- `pip install -r requirements.txt` - установка зависимостей
- `python manage.py migrate` - применение миграций
- `python manage.py runserver` - запуск сервера

### Linux/Macos:
- `python3 -m venv venv` - создание виртуального окружения
- `source venv/bin/activate` - активация виртуального окружения