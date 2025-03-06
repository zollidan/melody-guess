"""User model

Revision ID: 19630598e307
Revises: 5b6a685a9e87
Create Date: 2025-03-06 14:12:07.441076

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '19630598e307'
down_revision: Union[str, None] = '5b6a685a9e87'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('first_name', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('last_name', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('points', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'points')
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    op.drop_column('users', 'username')
    # ### end Alembic commands ###
