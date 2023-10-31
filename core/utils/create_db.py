from sqlalchemy import Column, Integer
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

from settings import Settings

Base = declarative_base()


class Subscriber(Base):
    __tablename__ = 'subscribers'

    id = Column(Integer, primary_key=True)


async def create():
    engine = create_async_engine(url=Settings.DATABASE_URL, echo=True)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    return engine


async def add_subscriber(user_id: int):
    engine = await create()
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async with async_session() as session:
        async with session.begin():
            subscriber = await session.get(Subscriber, user_id)
            if not subscriber:
                session.add(Subscriber(id=user_id))

        await session.commit()

    await engine.dispose()


async def remove_subscriber(user_id: int):
    engine = await create()
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async with async_session() as session:
        subscriber = await session.get(Subscriber, user_id)
        if subscriber:
            await session.delete(subscriber)
            await session.commit()

    await engine.dispose()


async def all_subscribers():
    engine = await create()
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    subscribers = []

    async with async_session() as session:
        stmt = select(Subscriber)
        result = await session.execute(stmt)
        subscribers = result.scalars().all()

    await engine.dispose()

    return subscribers
