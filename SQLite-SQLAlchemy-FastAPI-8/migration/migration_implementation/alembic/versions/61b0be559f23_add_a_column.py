"""Add a column

Revision ID: 61b0be559f23
Revises: 8fd3a4c574dc
Create Date: 2025-08-18 21:00:35.658982

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '61b0be559f23'
down_revision: Union[str, Sequence[str], None] = '8fd3a4c574dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column("transaction-date", sa.DateTime))



def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column(table_name='users', column_name='transaction-data')
