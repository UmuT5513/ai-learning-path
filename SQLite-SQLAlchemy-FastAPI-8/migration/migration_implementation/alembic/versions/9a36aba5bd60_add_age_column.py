"""add age column 

Revision ID: 9a36aba5bd60
Revises: 61b0be559f23
Create Date: 2025-08-18 23:44:09.073651

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a36aba5bd60'
down_revision: Union[str, Sequence[str], None] = '61b0be559f23'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column("age", sa.Integer))



def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column(table_name='users', column_name='age')