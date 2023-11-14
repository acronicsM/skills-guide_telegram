from sqlalchemy import select, Column, Integer
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

from settings import Settings

Base = declarative_base()


class Subscriber(Base):
    __tablename__ = 'subscribers'

    id = Column(Integer, primary_key=True)


async def create():
    db_url = f'postgresql+asyncpg://{Settings.POSTGRES_USER}:{Settings.POSTGRES_PASSWORD}@{Settings.POSTGRES_HOST}:{Settings.POSTGRES_PORT}/{Settings.POSTGRES_DATABASE}'
    engine = create_async_engine(url=db_url, echo=True)

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
