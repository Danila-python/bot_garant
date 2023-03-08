from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import Column, Integer, String, Boolean

from contextlib import asynccontextmanager
# SQLALCHEMY_DATABASE_URL = "sqlite:///users_data_base"


SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:root@localhost/telegram_users"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
Base = declarative_base()


class Users(Base):
    __tablename__ = "users"

    user_id = Column(String, unique=True, nullable=False)
    user_mobile_phone = Column(String, primary_key=True, nullable=False)
    active = Column(Boolean, default=True)


def async_session_generator():
    return sessionmaker(
        engine, class_=AsyncSession
    )


@asynccontextmanager
async def get_session():
    try:
        async_session = async_session_generator()

        async with async_session() as session:
            yield session
    except:
        await session.rollback()
        raise
    finally:
        await session.close()
