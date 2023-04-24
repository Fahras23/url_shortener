"""init

Revision ID: 3d98d8736c86
Revises: 
Create Date: 2023-04-24 11:55:47.631343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d98d8736c86'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'urls',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('inputUrl', sa.String, nullable=False),
        sa.Column('outputUrl', sa.String, nullable=False)
    )


def downgrade():
    op.drop_table('urls')