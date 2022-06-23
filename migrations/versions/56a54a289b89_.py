"""empty message

Revision ID: 56a54a289b89
Revises: b7efd48deaed
Create Date: 2022-06-17 00:28:41.659786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56a54a289b89'
down_revision = 'b7efd48deaed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('hits', 'artist_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('hits', 'artist_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###