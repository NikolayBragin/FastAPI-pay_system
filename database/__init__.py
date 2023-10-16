from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Ссылка на базу данных
# SQLALCHEMY_DATABASE_URI = "sqlite:///data.db"
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@database/postgres"

# Подключение к базе данных
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# Генерация сессии
SessionLocal = sessionmaker(bind=engine)

# Общий класс для моделей (models.py)
Base = declarative_base()

# Импорт моделей
from database import models

# Функция для генерации связей к базе данных
def get_db():
    db = SessionLocal()
    try:
        yield db

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


