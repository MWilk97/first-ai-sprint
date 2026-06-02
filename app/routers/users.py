from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.user import UserCreate, UserRead
from app.database import users_db


router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    # Check if user with this email already exists
    for existing_user in users_db:
        if existing_user["email"] == user.email:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User with this email already exists"
            )
    
    # Create new user
    new_user = {
        "id": len(users_db) + 1,
        "email": user.email,
        "full_name": user.full_name,
        "created_at": "2023-01-01T00:00:00"
    }
    
    users_db.append(new_user)
    return new_user