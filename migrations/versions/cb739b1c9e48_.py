"""empty message

Revision ID: cb739b1c9e48
Revises: a94d14a54d8b
Create Date: 2019-10-06 12:29:53.031990

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb739b1c9e48'
down_revision = 'a94d14a54d8b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('login', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('login'),
    sa.UniqueConstraint('login'),
    sa.UniqueConstraint('token')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
