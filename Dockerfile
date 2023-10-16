# Указываем язык программирования
FROM python:3.10

# Рабочая директория
WORKDIR /pay_system

# Копировать все папки/файлы в Докер
COPY . /pay_system

# Установка необходимых компонентов
RUN pip install -r requirements.txt

# Команда для запуска
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8080"]