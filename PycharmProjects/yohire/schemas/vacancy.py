from typing import Optional

from pydantic import BaseModel


# Базовая схема для вакансий (используется и для Create, и для Read)
class VacancyBase(BaseModel):
    title: str
    description: Optional[str] = None
    company: str
    location: str


# Схема для создания вакансии (POST)
class VacancyCreate(VacancyBase):
    pass


# Схема для чтения вакансии из БД (GET)
class VacancyRead(VacancyBase):
    id: int

    class Config:
        orm_mode = True
