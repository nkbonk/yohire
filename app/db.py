# app/db.py
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# 1) Читаем строку подключения из окружения; если вдруг нет, жёстко укажем host=db
raw = os.getenv("DATABASE_URL")
if not raw:
    raw = "postgresql+asyncpg://nkbonk:80395742Ks@db:5432/yohire_db"

# 2) Если кто-то засунул psycopg2-префикс, заменим его на asyncpg
DATABASE_URL = raw.replace("postgresql+psycopg2://", "postgresql+asyncpg://")

# 3) Создаём асинхронный движок и фабрику сессий
engine = create_async_engine(DATABASE_URL, future=True)
async_session = sessionmaker (engine, class_=AsyncSession, expire_on_commit=False)