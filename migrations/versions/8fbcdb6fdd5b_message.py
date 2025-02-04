"""message

Revision ID: 8fbcdb6fdd5b
Revises: 9f4e99f8ac45
Create Date: 2025-01-27 11:19:31.098677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fbcdb6fdd5b'
down_revision = '9f4e99f8ac45'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('restaurant_pizzas', sa.Column('restaurant_id', sa.Integer(), nullable=False))
    op.add_column('restaurant_pizzas', sa.Column('pizza_id', sa.Integer(), nullable=False))
    op.create_foreign_key(op.f('fk_restaurant_pizzas_pizza_id_pizzas'), 'restaurant_pizzas', 'pizzas', ['pizza_id'], ['id'])
    op.create_foreign_key(op.f('fk_restaurant_pizzas_restaurant_id_restaurants'), 'restaurant_pizzas', 'restaurants', ['restaurant_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_restaurant_pizzas_restaurant_id_restaurants'), 'restaurant_pizzas', type_='foreignkey')
    op.drop_constraint(op.f('fk_restaurant_pizzas_pizza_id_pizzas'), 'restaurant_pizzas', type_='foreignkey')
    op.drop_column('restaurant_pizzas', 'pizza_id')
    op.drop_column('restaurant_pizzas', 'restaurant_id')
    # ### end Alembic commands ###
