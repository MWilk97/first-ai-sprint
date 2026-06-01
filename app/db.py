from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create SQLite engine
engine = create_engine('sqlite:///carpool.sqlite', echo=True)

# Create declarative base
Base = declarative_base()

# Create database tables
Base.metadata.create_all(bind=engine)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    """FastAPI dependency to get database session"""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()