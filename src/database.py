from config import POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, DB_HOST, DB_PORT
from sqlalchemy import BigInteger, create_engine
# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column

DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{POSTGRES_DB}'
engine = create_engine(DATABASE_URI)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine) # , expire_on_commit=False


class BaseModel:
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)


Base = declarative_base(cls=BaseModel)
