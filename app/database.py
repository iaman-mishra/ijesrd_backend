from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import  DeclarativeBase
from core.config import settings

if settings.DB_URI is None or settings.DB_URI == "":
	raise ValueError("DB_URI Not Found")

engine = create_async_engine(
    settings.DB_URI,
    echo=settings.DEBUG, 
    pool_pre_ping=True,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

class Base(DeclarativeBase):
    pass