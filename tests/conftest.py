import pytest
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.db import engine, Base

# Create a test database
TEST_DATABASE_URL = "sqlite:///./test.db"

@pytest.fixture(scope="session")

def test_engine():
    """Create a test engine"""
    return create_engine(TEST_DATABASE_URL)


@pytest.fixture(scope="session")

def test_base():
    """Create a test base"""
    return Base


@pytest.fixture(scope="function")

def db_session(test_engine, test_base):
    """Create a database session for each test"""
    # Create all tables in the test database
    test_base.metadata.create_all(bind=test_engine)
    
    # Create a new session
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
    session = SessionLocal()
    
    try:
        yield session
    finally:
        session.close()
        # Drop all tables after test
        test_base.metadata.drop_all(bind=test_engine)