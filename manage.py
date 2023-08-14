import click
import asyncio
from pathlib import Path
import contextlib
from contextlib import contextmanager
from src.database import async_session, engine, Base
from sqlalchemy.sql import text

BASE_DIR = Path(__file__).parent


@click.group()
def cli():
    pass


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = async_session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


@cli.command()
def clear_db():
    with contextlib.closing(engine.connect()) as con:
        trans = con.begin()
        for table in reversed(Base.metadata.sorted_tables):
            con.execute(text(f'TRUNCATE TABLE {table} CASCADE;'))
        trans.commit()
