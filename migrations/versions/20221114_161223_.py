"""empty message

Revision ID: 4bf9f839e1da
Revises: 791af5f40ef3
Create Date: 2022-11-14 16:12:23.956421

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4bf9f839e1da'
down_revision = '791af5f40ef3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('path', sa.String(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_images')
    # ### end Alembic commands ###
