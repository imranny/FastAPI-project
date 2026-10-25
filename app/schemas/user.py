from typing import Optional

from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    """Схема для создания пользователя"""

    name: str
    age: int
    sex: Optional[str] = None
    job: Optional[str] = None


class UserRead(UserCreate):
    """Схема для чтения пользователя"""

    id: int
    model_config = ConfigDict(from_attributes=True)


class UserID(BaseModel):
    """Схема ответа с ID созданного пользователя"""

    ok: bool = True
    user_id: int