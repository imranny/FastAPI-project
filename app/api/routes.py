from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.db import get_session
from app.repositories import UserRepository
from app.schemas import UserCreate, UserID, UserRead

router = APIRouter(prefix="/users", tags=["Users"])

SessionDep = Annotated[AsyncSession, Depends(get_session)]


@router.post("", response_model=UserID, status_code=201)
async def add_user(data: UserCreate, session: SessionDep) -> UserID:
    """Создать нового пользователя."""
    user_id = await UserRepository.add_user(session, data)
    return UserID(user_id=user_id)


@router.get("", response_model=list[UserRead])
async def get_users(session: SessionDep) -> list[UserRead]:
    """Получить список всех пользователей."""
    return await UserRepository.get_all(session)