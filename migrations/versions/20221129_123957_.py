"""empty message

Revision ID: 45560712cfe6
Revises: 4bf9f839e1da
Create Date: 2022-11-29 12:39:57.595613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45560712cfe6'
down_revision = '4bf9f839e1da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('completed_orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('order_date', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('shipping_address_id', sa.Integer(), nullable=False),
    sa.Column('order_total', sa.Numeric(precision=16, scale=2), nullable=False),
    sa.Column('order_status', sa.String(length=40), nullable=False),
    sa.ForeignKeyConstraint(['shipping_address_id'], ['addresses.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_foreign_key(None, 'products', 'users', ['user_id'], ['id'])
    op.add_column('user_addresses', sa.Column('address_id', sa.Integer(), nullable=False))
    op.alter_column('user_addresses', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint('user_addresses_user_id_fkey', 'user_addresses', type_='foreignkey')
    op.create_foreign_key(None, 'user_addresses', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'user_addresses', 'addresses', ['address_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_addresses', type_='foreignkey')
    op.drop_constraint(None, 'user_addresses', type_='foreignkey')
    op.create_foreign_key('user_addresses_user_id_fkey', 'user_addresses', 'addresses', ['user_id'], ['id'])
    op.alter_column('user_addresses', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('user_addresses', 'address_id')
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.drop_table('completed_orders')
    # ### end Alembic commands ###
