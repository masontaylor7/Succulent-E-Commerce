"""empty message

Revision ID: 791af5f40ef3
Revises: 2c6878959ee6
Create Date: 2022-11-14 13:32:45.930158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '791af5f40ef3'
down_revision = '2c6878959ee6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    # ### end Alembic commands ###