# Тестовое задание для TraceCore

## Требования к окружению
- Python 3.11 или выше

## Установка

1. Клонируйте репозиторий:
`git clone https://github.com/klim9929/test_task_for_traceCORE.git`
`cd test_task_for_traceCORE`
2. Создайте виртуальное окружение: 
`python -m venv venv`
3. Активируйте виртуальное окружение: 
 Windows: `.venv\Scripts\activate`
 Linux/macOS: `source .venv/bin/activate`
4. Установите зависимости:
 `pip install -r requirements.txt`
5. Создайте файл `.env` в корне проекта и скопируйте содержимое `.env.example` в него. 


## Запуск тестов

Для запуска всех тестов используйте скрипт:
`python run_tests.py`
или выполнить файл `run_tests.py` в IDE

## Просмотр отчёта

После выполнения тестов:
1. Перейдите в папку `logs/`
2. Найдите файл с именем вида:  
   `test_run_2026-01-20_16-29-44.log`
3. Откройте его в любом текстовом редакторе