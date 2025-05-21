from sqlalchemy import Column, Integer, String, Text, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import os

Base = declarative_base()

class UserMemory(Base):
    __tablename__ = "user_memory"
    id = Column(Integer, primary_key=True)
    discord_id = Column(String, unique=True, index=True)
    memory = Column(Text)
    last_updated = Column(DateTime, default=datetime.utcnow)

def get_engine():
    from bot.utils.config import DATABASE_URL
    return create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def get_session():
    engine = get_engine()
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)()
