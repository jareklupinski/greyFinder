"""picture greyurls

Revision ID: 6c1c48e21056
Revises: 51a1393f7020
Create Date: 2020-02-01 23:28:07.835404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c1c48e21056'
down_revision = '51a1393f7020'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('picture', sa.Column('greyurl', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('picture', 'greyurl')
    # ### end Alembic commands ###
