"""add last few columns to posts table

Revision ID: 4569be085380
Revises: 4c605c4ca43e
Create Date: 2023-06-24 05:07:12.568124

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4569be085380'
down_revision = '4c605c4ca43e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
