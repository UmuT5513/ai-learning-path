"""add users and books tables

Revision ID: 8874cc862b2b
Revises: 3d9d946d56be
Create Date: 2025-08-20 19:11:32.754666

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8874cc862b2b'
down_revision: Union[str, Sequence[str], None] = '3d9d946d56be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
