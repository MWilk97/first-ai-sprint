import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db import Base, engine, get_session
from app.models.user import User


def test_create_all():
    # This test ensures that the database tables are created
    # Create a new engine for testing
    test_engine = create_engine('sqlite:///:memory:', echo=True)
    # Create all tables
    Base.metadata.create_all(bind=test_engine)
    # Verify that tables were created by checking if they exist
    assert test_engine.has_table('users')


def test_user_roundtrip():
    # Create a new engine for testing
    test_engine = create_engine('sqlite:///:memory:', echo=True)
    # Create all tables
    Base.metadata.create_all(bind=test_engine)
    
    # Create a session
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
    session = SessionLocal()
    
    # Create a new user
    user = User(username="testuser", email="test@example.com", full_name="Test User")
    session.add(user)
    session.commit()
    
    # Retrieve the user
    retrieved_user = session.query(User).filter(User.username == "testuser").first()
    
    # Verify the user was retrieved correctly
    assert retrieved_user.username == "testuser"
    assert retrieved_user.email == "test@example.com"
    assert retrieved_user.full_name == "Test User"
    
    session.close()
