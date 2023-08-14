from typing import List, Dict, Optional
from src.database import Base
from sqlalchemy import ForeignKey, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from datetime import datetime


class Post(Base):
    __tablename__ = "posts"
    title: Mapped[str]
    content: Mapped[str]
    creation_date: Mapped[datetime] = mapped_column(insert_default=func.now())

    telegram_id: Mapped[int | None]
    category_id: Mapped[int | None] = mapped_column(ForeignKey("posts_categories.id"))
    category: Mapped["Category"] = relationship(back_populates="posts")
    channel_id: Mapped[int | None] = mapped_column(ForeignKey("channels.id"))
    channel: Mapped["Channel"] = relationship(back_populates="posts")


class Category(Base):
    __tablename__ = 'posts_categories'
    name: Mapped[str | None]

    posts: Mapped[List["Post"]] = relationship(back_populates="category")


class Channel(Base):
    __tablename__ = "channels"
    name: Mapped[str | None]

    posts: Mapped[List["Post"]] = relationship(back_populates="channel")
