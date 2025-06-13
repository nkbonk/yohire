from dotenv import load_dotenv
import os

load_dotenv()

# Достаём URL БД из переменных окружения
DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('DATABASE_HOST')}:"
    f"{os.getenv('DATABASE_PORT')}/"
    f"{os.getenv('DATABASE_NAME')}"
)


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Vacancy, Base

# Движок, привязываем к нему echo=True, чтобы видеть SQL-запросы
engine = create_engine(DATABASE_URL, echo=True)

# Фабрика сессий для работы с БД
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Проверяю, что таблица точно появилась
Base.metadata.create_all(bind=engine)

def populate_test_data():
    """
    Функция создаёт несколько объектов Vacancy
    и скидывает их в базу.
    """
    # Новая сессия
    session = SessionLocal()

    try:
        fake_vacancies = [
            Vacancy(
                title="Junior Python Developer",
                description="Ищем начинающего Python-разработчика для стартапа."
            ),
            Vacancy(
                title="Middle Backend Engineer",
                description="Нужен опытный бэкендщик: FastAPI, PostgreSQL, Docker."
            ),
            Vacancy(
                title="Senior Data Scientist",
                description="Аналитика, машинное обучение, опыт с большими данными."
            ),
        ]

        session.add_all(fake_vacancies)
        session.commit()
        # Подтверждаю, что всё ок
        print(f"Inserted {len(fake_vacancies)} test vacancies.")

    except Exception as e:
        # Если проблема, делается коммит
        session.rollback()
        print("Error inserting test data:", e)
        raise

    finally:
        session.close()


# Запускаем функцию, если файл запущен как скрипт (ЧПТ подсказал)
if __name__ == "__main__":
    populate_test_data()