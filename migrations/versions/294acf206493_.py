"""empty message

Revision ID: 294acf206493
Revises: 
Create Date: 2023-05-16 12:58:39.848744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '294acf206493'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('great',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('origin', sa.String(length=80), nullable=False),
    sa.Column('birth', sa.String(length=80), nullable=False),
    sa.Column('death', sa.String(length=80), nullable=True),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('great')
    # ### end Alembic commands ###