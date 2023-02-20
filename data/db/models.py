from sqlalchemy import Column, Integer, String, Boolean

from data.db.base import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(String, Unique=True, nullable=False)
    user_mobile_phone = Column(String, Unique=True, nullable=False)
    active = Column(Boolean, default=True)
