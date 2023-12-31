"""rename

Revision ID: f5927a199d6e
Revises: ab09bf52ac41
Create Date: 2023-08-14 21:11:19.311547

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f5927a199d6e'
down_revision: Union[str, None] = 'ab09bf52ac41'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('telegram_id', sa.Integer(), nullable=True))
    op.add_column('posts_categories', sa.Column('name', sa.String(), nullable=False))
    op.drop_column('posts_categories', 'title')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts_categories', sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('posts_categories', 'name')
    op.drop_column('posts', 'telegram_id')
    # ### end Alembic commands ###
