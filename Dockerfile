# Используем базовый образ с поддержкой Python
FROM python:3.10.5

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем зависимости проекта (если есть файл requirements.txt)
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем остальные файлы проекта
COPY . .

# Экспортируем порт 80
EXPOSE 80

# Команда для запуска приложения
CMD ["python", "main.py"]
