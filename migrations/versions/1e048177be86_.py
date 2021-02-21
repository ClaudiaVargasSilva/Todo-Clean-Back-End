"""empty message

Revision ID: 1e048177be86
Revises: 
Create Date: 2021-02-19 14:18:03.653959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e048177be86'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comunas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.String(length=15), nullable=True),
    sa.Column('horas', sa.Integer(), nullable=True),
    sa.Column('vecesx_mes', sa.Integer(), nullable=True),
    sa.Column('precio', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rol', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('servicios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('precio', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rol_id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('rut', sa.String(length=15), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('last_name', sa.String(length=120), nullable=False),
    sa.Column('address', sa.String(length=180), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=True),
    sa.Column('birth_date', sa.DateTime(), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=False),
    sa.Column('password', sa.String(length=1000), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('fecha_registro', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['rol_id'], ['roles.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('rut')
    )
    op.create_table('documentos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('cert_antecedentes', sa.String(length=100), nullable=False),
    sa.Column('foto_cedula', sa.String(length=100), nullable=False),
    sa.Column('cert_domicilio', sa.String(length=100), nullable=False),
    sa.Column('cert_prevision', sa.String(length=100), nullable=False),
    sa.Column('cert_cotizacion', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('membresias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('plan_id', sa.Integer(), nullable=False),
    sa.Column('users_id', sa.Integer(), nullable=False),
    sa.Column('fecha_compra', sa.DateTime(), nullable=True),
    sa.Column('fecha_termino', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['plan_id'], ['planes.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pedidos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fecha_pedido', sa.DateTime(), nullable=True),
    sa.Column('users_id', sa.Integer(), nullable=True),
    sa.Column('trab_id', sa.Integer(), nullable=True),
    sa.Column('servicio_id', sa.Integer(), nullable=False),
    sa.Column('valor', sa.Integer(), nullable=False),
    sa.Column('id_comuna', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_comuna'], ['comunas.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['servicio_id'], ['servicios.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['trab_id'], ['users.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pedidos')
    op.drop_table('membresias')
    op.drop_table('documentos')
    op.drop_table('users')
    op.drop_table('servicios')
    op.drop_table('roles')
    op.drop_table('planes')
    op.drop_table('comunas')
    # ### end Alembic commands ###
