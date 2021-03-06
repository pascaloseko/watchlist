"""Initial Migration

Revision ID: 6880ca464954
Revises: 041743ee8f31
Create Date: 2018-02-01 12:21:16.021156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6880ca464954'
down_revision = '041743ee8f31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profile_photos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pic_path', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profile_photos')
    # ### end Alembic commands ###
