import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Завантажуємо змінні з .env файлу
load_dotenv()

# Отримуємо URL з середовища
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

if not SQLALCHEMY_DATABASE_URL:
    raise ValueError(
        "DATABASE_URL is not set. Please add it to your .env file or environment variables."
    )

# Запобіжник для сумісності з форматом postgres://
if SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Створюємо двигун з оптимізацією для serverless баз (Neon)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # pool_pre_ping змушує SQLAlchemy перевіряти з'єднання перед запитом
    # Це виправить помилку "SSL connection has been closed unexpectedly"
    pool_pre_ping=True,
    # pool_recycle оновлює з'єднання кожні 5 хвилин (300 секунд)
    pool_recycle=300,
)

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