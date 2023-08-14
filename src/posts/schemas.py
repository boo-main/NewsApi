from pydantic import BaseModel


class Category(BaseModel):
    id: int
    name: str | None = None


class Channel(BaseModel):
    id: int
    name: str | None = None


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    telegram_id: int | None = None
    category_id: int | None = None
    channel_id: int | None = None


class Post(PostBase):
    id: int
    category: Category | None = None
    channel: Channel | None = None

    class Config:
        from_attributes = True
