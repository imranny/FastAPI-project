from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User
from app.schemas import UserCreate, UserRead


class UserRepository:
    """Репозиторий для работы с пользователями."""

    @staticmethod
    async def add_user(session: AsyncSession, data: UserCreate) -> int:
        """Добавить нового пользователя и вернуть его ID."""
        user = User(**data.model_dump())
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user.id

    @staticmethod
    async def get_all(session: AsyncSession) -> list[UserRead]:
        """Получить всех пользователей."""
        result = await session.execute(select(User))
        users = result.scalars().all()
        return [UserRead.model_validate(user) for user in users]