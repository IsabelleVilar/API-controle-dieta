"""Inicialização da base de dados

Revision ID: ed3d9377f3ec
Revises: 
Create Date: 2024-03-21 16:31:59.789327

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed3d9377f3ec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('refeicao',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('descricao', sa.Text(), nullable=True),
    sa.Column('data_hora', sa.DateTime(), nullable=False),
    sa.Column('esta_na_dieta', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('refeicao')
    # ### end Alembic commands ###
