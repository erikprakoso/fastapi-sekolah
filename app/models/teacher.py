from sqlalchemy import Column, Integer, String
from config import Base

class Teacher(Base):
    __tablename__ = 'teacher'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    subject = Column(String(100))
    email = Column(String(100))