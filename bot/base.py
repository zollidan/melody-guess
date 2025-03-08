from typing import List, Any, TypeVar, Generic
from pydantic import BaseModel
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from sqlalchemy import update as sqlalchemy_update, delete as sqlalchemy_delete, func
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession
from bot.database import Base
from typing import TypeVar
from bot.model import User, HummingSample

T = TypeVar("T", bound=Base)

class BaseDAO(Generic[T]):
    model: type[T]
    
    @classmethod
    async def find_one_or_none_by_id(cls, data_id: str, session: AsyncSession):
        logger.info(f"Поиск {cls.model.__name__} с ID: {data_id}")
        try:
            query = select(cls.model).filter_by(id=data_id)
            result = await session.execute(query)
            record = result.scalar_one_or_none()
            if record:
                logger.info(f"Запись с ID {data_id} найдена.")
            else:
                logger.info(f"Запись с ID {data_id} не найдена.")
            return record
        except SQLAlchemyError as e:
            logger.error(f"Ошибка при поиске записи с ID {data_id}: {e}")
            raise
        
    @classmethod
    async def find_one_or_none(cls, session: AsyncSession, filters: BaseModel):
        filter_dict = filters.model_dump(exclude_unset=True)
        logger.info(f"Поиск одной записи {cls.model.__name__} по фильтрам: {filter_dict}")
        try:
            query = select(cls.model).filter_by(**filter_dict)
            result = await session.execute(query)
            record = result.scalar_one_or_none()
            if record:
                logger.info(f"Запись найдена по фильтрам: {filter_dict}")
            else:
                logger.info(f"Запись не найдена по фильтрам: {filter_dict}")
            return record
        except SQLAlchemyError as e:
            logger.error(f"Ошибка при поиске записи по фильтрам {filter_dict}: {e}")
            raise
        
    @classmethod
    async def add(cls, session: AsyncSession, values: BaseModel):
        # Добавить одну запись
        values_dict = values.model_dump(exclude_unset=True)
        logger.info(f"Добавление записи {cls.model.__name__} с параметрами: {values_dict}")
        new_instance = cls.model(**values_dict)
        session.add(new_instance)
        try:
            await session.flush()
            logger.info(f"Запись {cls.model.__name__} успешно добавлена.")
        except SQLAlchemyError as e:
            await session.rollback()
            logger.error(f"Ошибка при добавлении записи: {e}")
            raise e
        return new_instance

class UserDAO(BaseDAO[User]):
    model = User
    
    @classmethod
    async def find_by_points_desc(cls, session: AsyncSession):
        logger.info(f"Поиск записей {cls.model.__name__} с сортировкой по количеству очков")
        try:
            query = select(cls.model).order_by(cls.model.points.desc()).limit(10)
            result = await session.execute(query)
            records = result.scalars().all()
            logger.info(f"Найдено {len(records)} с сортировкой по количеству очков")
            return records
        except SQLAlchemyError as e:
            logger.error(f"Ошибка при поиске записей в {cls.model.__name__}.")
            raise
        
class HummingSampleDAO(BaseDAO[HummingSample]):
    model = HummingSample
    
    @classmethod
    async def user_has_samples(cls, session: AsyncSession, user_id: int) -> bool:
        logger.info(f"Проверка наличия сэмплов у пользователя {user_id}")
        try:
            query = select(cls.model).where(cls.model.user_id == user_id).limit(1)
            result = await session.execute(query)
            sample = result.scalar_one_or_none()
            has_samples = sample is not None
            return has_samples
        except SQLAlchemyError as e:
            logger.error(f"Ошибка при проверке сэмплов у пользователя {user_id}: {e}")
            return False