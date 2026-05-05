# Використовуємо легкий офіційний образ Python
FROM python:3.12-slim

# Встановлюємо робочу директорію в контейнері
WORKDIR /app

# Копіюємо файл залежностей та встановлюємо їх
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь наш код у контейнер
COPY . .

# Команда для запуску сервера
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]