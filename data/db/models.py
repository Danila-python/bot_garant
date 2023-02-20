from sqlalchemy import Column, INTEGER, String

from data.db.base import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    user_id = Column(String)
