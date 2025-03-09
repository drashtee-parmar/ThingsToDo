from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# Define database URL (Update with your credentials)
DATABASE_URL = "postgresql://username:password@localhost:5432/event_db"

# Create a database engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the base class for ORM models
Base = declarative_base()
