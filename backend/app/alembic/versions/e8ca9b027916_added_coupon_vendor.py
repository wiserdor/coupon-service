"""added coupon vendor

Revision ID: e8ca9b027916
Revises: 7336f71b8752
Create Date: 2021-03-25 11:52:24.753249-07:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8ca9b027916'
down_revision = '7336f71b8752'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('coupon', sa.Column('dress_vendor', sa.String(), nullable=True))
    op.add_column('coupon', sa.Column('hair_vendor', sa.String(), nullable=True))
    op.add_column('coupon', sa.Column('makeup_vendor', sa.String(), nullable=True))
    op.alter_column('coupon', 'phone',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('coupon', 'phone',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('coupon', 'makeup_vendor')
    op.drop_column('coupon', 'hair_vendor')
    op.drop_column('coupon', 'dress_vendor')
    # ### end Alembic commands ###