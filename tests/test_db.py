import pytest
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.db import get_session, engine, Base
from app.models.user import User


def test_create_all():
    # This test ensures that the database tables are created
    # We'll check if the users table exists
    from sqlalchemy import inspect
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    assert 'users' in tables


def test_user_roundtrip():
    # Create a new user
    user_data = {
        'email': 'test@example.com',
        'full_name': 'Test User'
    }
    
    # Insert user
    user = User(**user_data)
    session = next(get_session())
    session.add(user)
    session.commit()
    session.refresh(user)
    
    # Retrieve user
    retrieved_user = session.query(User).filter(User.email == 'test@example.com').first()
    
    # Verify
    assert retrieved_user is not None
    assert retrieved_user.email == 'test@example.com'
    assert retrieved_user.full_name == 'Test User'
    
    # Clean up
    session.delete(user)
    session.commit()
    session.close()