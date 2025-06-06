from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()
# Это база для всех моделей SQLAlchemy.
# Она позволяет превращать классы Python в таблицы базы данных.


class Vacancy(Base):
    __tablename__ = "vacancies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(256), nullable=False)
    description = Column(Text, nullable=True)
    company = Column(String(256), nullable=False)
    location = Column(String(256), nullable=False)
