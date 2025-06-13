from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, Text

class Vacancy(Base):
    __tablename__ = "vacancies"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String(255),
        nullable=False,
        index=True
    )

    description = Column(
        Text,
        nullable=False
    )