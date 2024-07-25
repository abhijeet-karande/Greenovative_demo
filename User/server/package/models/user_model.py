from sqlalchemy import Column, Integer, String
from db.connections import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String, index=True)
    salary = Column(Integer)
    login_id = Column(String, unique=True, index=True)
    password = Column(String)