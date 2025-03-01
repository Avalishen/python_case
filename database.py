from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite+aiosqlite:///./db.db"

# Создаём асинхронный движок
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Создаём сессию
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# ✅ Определяем Base (чтобы Alembic знал про таблицы)
Base = declarative_base()

# Функция для получения сессии
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
