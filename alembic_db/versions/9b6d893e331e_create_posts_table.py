"""create posts table

Revision ID: 9b6d893e331e
Revises: 
Create Date: 2023-06-23 14:29:13.759048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b6d893e331e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():  
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
