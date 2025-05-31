# app/models.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

# ─────────────── Выносим Base в models.py ───────────────
Base = declarative_base()


class Vacancy(Base):
    __tablename__ = "vacancies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(256), nullable=False)
    description = Column(Text, nullable=True)
    company = Column(String(256), nullable=False)
    location = Column(String(256), nullable=False)