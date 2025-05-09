# app/repositories/base.py

import logging
from typing import Generic, TypeVar, Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from db.base_class import Base

logger = logging.getLogger(__name__)

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    """
    Basic repository with common CRUD operations:
    - get(id)
    - get_all()
    - delete(id)
    """

    def __init__(self, model: Type[ModelType], session: AsyncSession):
        """
        :param model: SQLAlchemy model
        :param session: asynchronous session SQLAlchemy
        """
        self.model = model
        self.session = session

    async def get(self, id: int) -> ModelType | None:
        """Get object by ID"""
        logger.debug("Base repo: fetching %s (id=%s)", self.model.__name__, id)
        stmt = select(self.model).where(self.model.id == id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_all(self) -> list[ModelType]:
        """Get all objects in the model"""
        logger.debug("Base repo: fetching all records of %s", self.model.__name__)
        stmt = select(self.model)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def delete(self, id: int, commit: bool = True) -> bool:
        """Delete object by ID"""
        logger.debug("Base repo: attempting to delete %s (id=%s)", self.model.__name__, id)
        obj = await self.get(id)
        if not obj:
            logger.debug("Base repo: %s (id=%s) not found", self.model.__name__, id)
            return False
        await self.session.delete(obj)
        if commit:
            await self.session.commit()
        logger.debug("Base repo: %s (id=%s) deleted", self.model.__name__, id)
        return True
