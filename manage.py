import click
import asyncio
import pandas
import datetime
import contextlib
from contextlib import contextmanager
from src.database import engine, session
from src.posts import models
from sqlalchemy.sql import text
from sqlalchemy import select
from config import BASE_DIR


@click.group()
def cli():
    pass


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    db = session()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


@cli.command()
def clear_db():
    with contextlib.closing(engine.connect()) as con:
        trans = con.begin()
        for table in reversed(models.Base.metadata.sorted_tables):
            con.execute(text(f'TRUNCATE TABLE {table} CASCADE;'))
        trans.commit()


@cli.command()
@click.argument('filename', default='demo.xlsx')
def load_from_xlsx(filename):
    full_path = BASE_DIR / "upload" / filename
    excel_data = pandas.read_excel(
        full_path,
        usecols='A:G',
        names=['id', 'telegram_id', 'content', 'creation_date', 'category_id', 'channel_id', 'title']
    )
    posts = excel_data.to_dict('records')
    # max_rows = 5
    with session_scope() as session:
        for num, post_data in enumerate(posts, 1):
            try:
                int(post_data['id'])
            except ValueError:
                print("skip post, incorrect format")
                print(post_data)
                continue
            try:
                int(post_data["channel_id"])
            except ValueError:
                del post_data['channel_id']
            else:
                channel = session.scalar(select(models.Channel).where(models.Channel.id == post_data["channel_id"]))
                if channel is None:
                    new_channel = models.Channel(id=post_data["channel_id"])
                    session.add(new_channel)
                    session.commit()

            try:
                int(post_data["category_id"])
            except ValueError:
                del post_data['category_id']
            else:
                category = session.scalar(select(models.Channel).where(models.Category.id == post_data["category_id"]))
                if category is None:
                    new_categoey = models.Category(id=post_data["category_id"])
                    session.add(new_categoey)
                    session.commit()
            try:
                datetime.datetime.fromisoformat(str(post_data['creation_date']))
            except ValueError:
                print("skip post, incorrect date format")
                print(post_data)
                continue
            post = models.Post(**post_data)
            session.add(post)
            session.commit()


if __name__ == '__main__':
    cli()
