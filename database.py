import os
from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


DATABASE_URL = "sqlite:///bot_data.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class UserQuery(Base):
    __tablename__ = "user_queries"

    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer, index=True)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow())


def init_db():
    Base.metadata.create_all(bind=engine)
