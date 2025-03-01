from sqlalchemy import Column, Integer, String, DateTime, func, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TaskDB(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(String(1024), nullable=True)

    # Устанавливаем время по МСК (UTC+3)
    created_at = Column(DateTime, server_default=text("(datetime('now', '+3 hours'))"))
    updated_at = Column(DateTime, server_default=text("(datetime('now', '+3 hours'))"), onupdate=text("(datetime('now', '+3 hours'))"))
