import pytest
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.db import Base, engine as app_engine

# Create a test database engine
TEST_DATABASE_URL = "sqlite:///./test.db"

# Create test engine
test_engine = create_engine(TEST_DATABASE_URL, echo=True)

# Create test session factory
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


@pytest.fixture(scope="session")

def test_db_engine():
    """Create test database engine"""
    return test_engine


@pytest.fixture(scope="function")

def db_session(test_db_engine):
    """Create database session for each test"""
    # Create all tables
    Base.metadata.create_all(bind=test_db_engine)
    
    # Create a new session for this test
    session = TestSessionLocal()
    try:
        yield session
    finally:
        session.close()
        # Drop all tables after test
        Base.metadata.drop_all(bind=test_db_engine)


@pytest.fixture(scope="session")

def engine():
    """Provide the main application engine"""
    return app_engine


@pytest.fixture(scope="session")

def base():
    """Provide the main application Base"""
    return Base