"""HummingSample

Revision ID: f65b4c159be2
Revises: 19630598e307
Create Date: 2025-03-08 21:38:22.632213

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f65b4c159be2'
down_revision: Union[str, None] = '19630598e307'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('humming_samples',
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('file_id', sa.Text(), nullable=False),
    sa.Column('song_title', sa.Text(), nullable=False),
    sa.Column('song_artist', sa.Text(), nullable=False),
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.telegram_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('humming_samples')
    # ### end Alembic commands ###
