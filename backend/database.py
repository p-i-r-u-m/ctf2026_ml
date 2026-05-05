import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Завантажуємо змінні з .env файлу
load_dotenv()

# Отримуємо URL з середовища БЕЗ хардкоду паролів у коді.
# Якщо змінної немає, програма видасть помилку при старті — це надійніше.
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

if not SQLALCHEMY_DATABASE_URL:
    raise ValueError(
        "DATABASE_URL is not set. Please add it to your .env file or environment variables."
    )

# Запобіжник для сумісності SQLAlchemy з деякими хмарними URL (наприклад, Render/Heroku)
# Вони часто видають 'postgres://', але драйвер psycopg2 вимагає 'postgresql://'
if SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Створюємо двигун.
# Для PostgreSQL (особливо в хмарі Neon) важливо використовувати правильний драйвер.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Створюємо фабрику сесій
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовий клас для моделей
Base = declarative_base()

# Dependency для FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()