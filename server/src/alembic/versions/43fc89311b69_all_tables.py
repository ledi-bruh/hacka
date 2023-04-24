"""all tables

Revision ID: 43fc89311b69
Revises: 
Create Date: 2023-04-24 11:38:52.565510

"""
from alembic import op
import sqlalchemy as sa
from fastapi_utils.guid_type import GUID
from src.core.settings import settings


# revision identifiers, used by Alembic.
revision = '43fc89311b69'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(sa.schema.CreateSchema(settings.db_schema))
    
    op.create_table('observations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('department_id', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='hacka'
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='hacka'
    )
    op.create_table('work_exp',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='hacka'
    )
    op.create_table('workers',
    sa.Column('guid', GUID(), nullable=False),
    sa.Column('fio', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('phone_number', sa.String(), nullable=False),
    sa.Column('work_exp_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['work_exp_id'], ['hacka.work_exp.id'], name='fk_workers__work_exp_id', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('guid'),
    schema='hacka'
    )
    op.create_table('work_status',
    sa.Column('worker_guid', GUID(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('attraction_year', sa.Integer(), nullable=False),
    sa.Column('observation_id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['observation_id'], ['hacka.observations.id'], name='fk_work_status__observation_id', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['post_id'], ['hacka.posts.id'], name='fk_work_status__post_id', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['worker_guid'], ['hacka.workers.guid'], name='fk_work_status__worker_guid', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('worker_guid', 'post_id', 'attraction_year', 'observation_id', 'code'),
    schema='hacka'
    )
    op.create_table('worker_post',
    sa.Column('worker_guid', GUID(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['hacka.posts.id'], name='fk_worker_post__post_id', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['worker_guid'], ['hacka.workers.guid'], name='fk_worker_post__worker_guid', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('worker_guid', 'post_id'),
    schema='hacka'
    )


def downgrade() -> None:
    op.drop_table('worker_post', schema='hacka')
    op.drop_table('work_status', schema='hacka')
    op.drop_table('workers', schema='hacka')
    op.drop_table('work_exp', schema='hacka')
    op.drop_table('posts', schema='hacka')
    op.drop_table('observations', schema='hacka')
    op.execute(sa.schema.DropSchema(settings.db_schema))
