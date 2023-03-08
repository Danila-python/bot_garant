# from sqlalchemy import Column, Integer, String, Boolean
#
# from data.db.base import Base
#
#
# class Users(Base):
#     __tablename__ = "users"
#
#     id = Column(Integer, index=True, autoincrement=True)
#     user_id = Column(String, unique=True, nullable=False)
#     user_mobile_phone = Column(String, primary_key=True, nullable=False)
#     active = Column(Boolean, default=True)
