from dotenv import load_dotenv
import os

load_dotenv()  # ищет .env в корне проекта

# Доставляем каждую переменную по её ключу
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")

DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:"
    f"{POSTGRES_PASSWORD}@"
    f"{DATABASE_HOST}:"
    f"{DATABASE_PORT}/"
    f"{DATABASE_NAME}"
)


    
from models import Base
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = FastAPI()  # стартуем FastAPI-сервер

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)       # создаём таблицы, если их нет

app = FastAPI()

@app.get("/")
def read_root():
    """
    Чекаем, что всё живо:
    возвращаем простое сообщение.
    """
    return {"message": "Yohire backend is up with .env!"}