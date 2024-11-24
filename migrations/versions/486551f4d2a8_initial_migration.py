"""Initial migration

Revision ID: 486551f4d2a8
Revises: fd2be582fa9a
Create Date: 2024-11-22 17:39:30.848952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '486551f4d2a8'
down_revision = 'fd2be582fa9a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('powers')
    op.drop_table('heroes')
    op.drop_table('hero_powers')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hero_powers',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('strength', sa.VARCHAR(length=20), nullable=True),
    sa.Column('hero_id', sa.INTEGER(), nullable=False),
    sa.Column('power_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['hero_id'], ['heroes.id'], ),
    sa.ForeignKeyConstraint(['power_id'], ['powers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('heroes',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=True),
    sa.Column('super_name', sa.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('powers',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=True),
    sa.Column('description', sa.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###