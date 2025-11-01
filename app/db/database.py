import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

from app.utils.helpers import log_message
load_dotenv()  # Load .env file

# Build connection string dynamically
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib

params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-7NB8KQQ\\SQLEXPRESS;"
    "DATABASE=OrgDB;"
    "UID=pythonuser;"
    "PWD=Password1234"
)

# Create SQLAlchemy engine
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency (for FastAPI)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
