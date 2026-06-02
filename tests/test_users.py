import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.schemas.user import UserCreate

client = TestClient(app)

def test_create_user_happy_path():
    response = client.post(
        "/users/",
        json={
            "email": "test@example.com",
            "full_name": "Test User"
        }
    )
    assert response.status_code == 201
    assert response.json()["email"] == "test@example.com"
    assert response.json()["full_name"] == "Test User"


def test_create_user_duplicate_email():
    # Create a user first
    client.post(
        "/users/",
        json={
            "email": "duplicate@example.com",
            "full_name": "Duplicate User"
        }
    )
    
    # Try to create another user with the same email
    response = client.post(
        "/users/",
        json={
            "email": "duplicate@example.com",
            "full_name": "Another User"
        }
    )
    assert response.status_code == 409
    assert response.json()["detail"] == "User with this email already exists"


def test_create_user_invalid_email():
    response = client.post(
        "/users/",
        json={
            "email": "invalid-email",
            "full_name": "Invalid Email User"
        }
    )
    assert response.status_code == 422