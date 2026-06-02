from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create SQLite engine
engine = create_engine('sqlite:///./carpool.sqlite', connect_args={'check_same_thread': False})

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for declarative models
Base = declarative_base()


def get_session():
    """FastAPI dependency to get a database session."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()