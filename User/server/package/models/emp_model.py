from sqlalchemy import Column, Integer, String
from db.connections import Base

class Emp(Base):
    __tablename__ = 'empInfo'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    city = Column(String, index=True)
    salary = Column(Integer)