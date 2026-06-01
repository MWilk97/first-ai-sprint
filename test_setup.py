from app.db import engine, Base
from app.models.user import User

print("Testing database setup...")

# Test that we can access the engine and Base
print(f"Engine: {engine}")
print(f"Base: {Base}")

# Test that we can create tables
Base.metadata.create_all(bind=engine)
print("Database tables created successfully")

# Test that we can create a user
user = User(name="Test User", email="test@example.com", phone="1234567890")
print(f"User created: {user.name}, {user.email}, {user.phone}")

print("All tests passed!")