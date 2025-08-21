"""users_and_books

Revision ID: 3d9d946d56be
Revises: 7580dcc33794
Create Date: 2025-08-20 12:20:30.866892

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d9d946d56be'
down_revision: Union[str, Sequence[str], None] = '7580dcc33794'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
