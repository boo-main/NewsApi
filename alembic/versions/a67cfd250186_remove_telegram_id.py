"""remove telegram_id

Revision ID: a67cfd250186
Revises: 833fa1a28e83
Create Date: 2023-08-15 17:19:08.592019

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a67cfd250186'
down_revision: Union[str, None] = '833fa1a28e83'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'telegram_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('telegram_id', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
