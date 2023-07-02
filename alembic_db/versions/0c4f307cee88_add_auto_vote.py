"""add auto-vote

Revision ID: 0c4f307cee88
Revises: 4569be085380
Create Date: 2023-06-24 06:02:00.668406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c4f307cee88'
down_revision = '4569be085380'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('post_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(
                        ['post_id'], ['posts.id'], ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(
                        ['user_id'], ['users.id'], ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('user_id', 'post_id')
                    )
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    op.drop_constraint('owner_id', 'posts', type_='foreignkey')
    op.create_foreign_key(None, 'posts', 'users', ['owner_id'], [
                          'id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.create_foreign_key('owner_id', 'posts', 'users', ['owner_id'], ['id'])
    op.drop_column('posts', 'content')
    op.drop_table('votes')
    # ### end Alembic commands ###
