from sqlalchemy import Boolean, Column, Integer, String
from app.db import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(225),nullable=False, index=True)
    description = Column(String(1000),nullable=True)
    completed = Column(Boolean,default=False, nullable=False)

