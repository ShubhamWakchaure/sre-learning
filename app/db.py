from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env.local")

# Fallback to SQLite if not set
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
print("DB URL:", DATABASE_URL)

# Create test.db file if using SQLite and it doesn't exist
if DATABASE_URL.startswith("sqlite") and not os.path.exists("test.db"):
    print("Creating temporary SQLite test DB")
    open("test.db", "a").close()

# Avoid threading issues with SQLite
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
