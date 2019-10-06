"""empty message

Revision ID: a94d14a54d8b
Revises: 725b8cec182c
Create Date: 2019-10-05 21:10:51.589691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a94d14a54d8b'
down_revision = '725b8cec182c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('call',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('date', sa.Integer(), nullable=False),
    sa.Column('duration_answer', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('phone_number_client', sa.String(), nullable=False),
    sa.Column('phone_number_operator', sa.String(), nullable=False),
    sa.Column('hand_up_initiator', sa.String(), nullable=True),
    sa.Column('transfers', sa.String(), nullable=True),
    sa.Column('transfers_count', sa.Integer(), nullable=True),
    sa.Column('holds_count', sa.Integer(), nullable=True),
    sa.Column('holds_duration', sa.Integer(), nullable=True),
    sa.Column('record_url', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['phone_number_operator'], ['operator.phone_number'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('call')
    # ### end Alembic commands ###
