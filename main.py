from src.database import session
from src.posts import schemas, models
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

app = FastAPI()


# Dependency
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts/", response_model=list[schemas.Post])
def get_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    select_query = select(models.Post).offset(skip).limit(limit)
    posts = db.scalars(select_query).all()
    return posts


@app.get("/posts/{post_id}", response_model=schemas.Post)
def get_post_by_id(post_id: int, db: Session = Depends(get_db)):
    db_post = db.scalar(select(models.Post).where(models.Post.id == post_id))
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@app.post("/posts/", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    channel = db.scalar(select(models.Channel).where(models.Channel.id == post.channel_id))
    if channel is None:
        new_channel = models.Channel(id=post.channel_id)
        db.add(new_channel)
        db.commit()
    category = db.scalar(select(models.Channel).where(models.Category.id == post.category_id))
    if category is None:
        new_categoey = models.Category(id=post.category_id)
        db.add(new_categoey)
        db.commit()
    db_post = models.Post(**post.model_dump())
    db.add(db_post)
    db.commit()
    return db_post
