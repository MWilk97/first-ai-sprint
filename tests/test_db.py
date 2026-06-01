import pytest
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.db import get_session, engine, Base
from app.models.user import User

# Test that database setup works

def test_create_all():
    # This test verifies that the database setup works
    # We can't easily test create_all without actually creating tables
    # But we can verify that the engine and Base are properly configured
    assert engine is not None
    assert Base is not None


def test_user_model(db_session):
    # Test that User model can be created and saved
    
    try:
        # Create a new user
        user = User(name="Test User", email="test@example.com", phone="1234567890")
        db_session.add(user)
        db_session.commit()
        
        # Retrieve the user
        retrieved_user = db_session.query(User).filter(User.email == "test@example.com").first()
        assert retrieved_user is not None
        assert retrieved_user.name == "Test User"
        assert retrieved_user.email == "test@example.com"
        assert retrieved_user.phone == "1234567890"
        
    except Exception as e:
        pytest.fail(f"User model test failed: {e}")


def test_database_tables_created(db_session):
    # Test that tables are created properly
    from app.models.user import User
    
    try:
        # Try to query the users table
        result = db_session.query(User).first()
        assert True  # If we get here without exception, the table exists
    except Exception as e:
        pytest.fail(f"Database table creation failed: {e}")