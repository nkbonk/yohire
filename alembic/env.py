from logging.config import fileConfig
from sqlalchemy.ext.asyncio import create_async_engine
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.models import Base
from sqlalchemy import create_engine
from app.db import DATABASE_URL
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context


config = context.config

if os.getenv("DATABASE_URL"):
    config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata



def run_migrations_offline() -> None:

    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()




def run_migrations_online() -> None:
    # 1) Собираем URL — сначала из env, иначе из ini
    url = os.getenv("DATABASE_URL", config.get_main_option("sqlalchemy.url"))
    # 2) Создаём простой синхронный движок
    connectable = create_engine(url, poolclass=pool.NullPool)

    # 3) Делаем миграции
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()