"""empty message

Revision ID: 725b8cec182c
Revises: 
Create Date: 2019-10-03 11:51:15.525612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '725b8cec182c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('operator',
    sa.Column('phone_number', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('phone_number'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('operator')
    # ### end Alembic commands ###
