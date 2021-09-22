"""AddTabelasAuxiliares

Revision ID: 159aa59a240b
Revises: a62b9690df62
Create Date: 2021-09-21 20:53:42.726214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '159aa59a240b'
down_revision = 'a62b9690df62'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dosagem_pobre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('alfa', sa.Integer(), nullable=True),
    sa.Column('c_unitario', sa.Integer(), nullable=True),
    sa.Column('a_unitario', sa.Integer(), nullable=True),
    sa.Column('b_unitario', sa.Integer(), nullable=True),
    sa.Column('c_massa', sa.Integer(), nullable=True),
    sa.Column('a_massa', sa.Integer(), nullable=True),
    sa.Column('b_massa', sa.Integer(), nullable=True),
    sa.Column('c_acr', sa.Integer(), nullable=True),
    sa.Column('a_acr', sa.Integer(), nullable=True),
    sa.Column('agua', sa.Integer(), nullable=True),
    sa.Column('ensaio_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ensaio_id'], ['ensaios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dosagem_rico',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('alfa', sa.Integer(), nullable=True),
    sa.Column('c_unitario', sa.Integer(), nullable=True),
    sa.Column('a_unitario', sa.Integer(), nullable=True),
    sa.Column('b_unitario', sa.Integer(), nullable=True),
    sa.Column('c_massa', sa.Integer(), nullable=True),
    sa.Column('a_massa', sa.Integer(), nullable=True),
    sa.Column('b_massa', sa.Integer(), nullable=True),
    sa.Column('c_acr', sa.Integer(), nullable=True),
    sa.Column('a_acr', sa.Integer(), nullable=True),
    sa.Column('agua', sa.Integer(), nullable=True),
    sa.Column('ensaio_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ensaio_id'], ['ensaios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dosagem_rico')
    op.drop_table('dosagem_pobre')
    # ### end Alembic commands ###