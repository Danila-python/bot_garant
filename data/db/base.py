from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import Column, Integer, String, Boolean

# SQLALCHEMY_DATABASE_URL = "sqlite:///users_data_base"


SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:root@localhost/telegram_users"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
Base = declarative_base()
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, index=True, autoincrement=True)
    user_id = Column(String, unique=True, nullable=False)
    user_mobile_phone = Column(String, primary_key=True, nullable=False)
    active = Column(Boolean, default=True)
