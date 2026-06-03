from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "sqlite:///./test.db"

engine = create_engine(db_url)

session_local = sessionmaker(bind=engine, autoflush=False, autocommit=False)
