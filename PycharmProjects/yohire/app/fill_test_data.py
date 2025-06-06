import asyncio

from app.db import async_session
from app.models import Vacancy  # ↰ берём модель и Base тоже (если надо)


async def create_test_data():
    async with async_session() as session:
        # создаём несколько вакансий
        test_list = [
            Vacancy(
                title="Python Developer",
                description="Работа над API",
                company="ABC Corp",
                location="Almaty",
            ),
            Vacancy(
                title="Frontend Engineer",
                description="React/Vue разработка",
                company="XYZ LLC",
                location="Astana",
            ),
            Vacancy(
                title="DevOps Specialist",
                description="CI/CD, Docker, K8s",
                company="123 StartUp",
                location="Shymkent",
            ),
        ]
        session.add_all(test_list)
        await session.commit()
        print(f"Inserted {len(test_list)} vacancies.")


if __name__ == "__main__":
    # Нужно запускать асинхронно
    asyncio.run(create_test_data())
