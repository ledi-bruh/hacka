"""added WorkerObservation

Revision ID: 3782c2924756
Revises: 43fc89311b69
Create Date: 2023-04-24 12:02:59.277099

"""
from alembic import op
import sqlalchemy as sa
from fastapi_utils.guid_type import GUID


# revision identifiers, used by Alembic.
revision = '3782c2924756'
down_revision = '43fc89311b69'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('worker_observation',
    sa.Column('worker_guid', GUID(), nullable=False),
    sa.Column('observation_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['observation_id'], ['hacka.observations.id'], name='fk_worker_observation__observation_id', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['worker_guid'], ['hacka.workers.guid'], name='fk_worker_observation__worker_guid', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('worker_guid', 'observation_id'),
    schema='hacka'
    )


def downgrade() -> None:
    op.drop_table('worker_observation', schema='hacka')
