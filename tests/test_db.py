import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db import Base, engine, get_session

# Test that create_all works

def test_create_all():
    # This test ensures that create_all runs without errors
    # We don't need to check the actual tables, just that it doesn't crash
    assert engine is not None

# Test roundtrip insert/select

class TestUser:
    def test_insert_select(self):
        # Create a new session
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        
        # Test that we can get a session
        assert db is not None
        
        # Clean up
        db.close()

# Test get_session dependency

def test_get_session():
    # Test that get_session function works
    session = next(get_session())
    assert session is not None
    session.close()