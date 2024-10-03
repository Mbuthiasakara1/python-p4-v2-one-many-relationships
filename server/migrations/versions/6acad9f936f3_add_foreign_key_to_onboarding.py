"""add foreign key to onboarding

Revision ID: 6acad9f936f3
Revises: eab3d6b5798c
Create Date: 2024-10-03 17:20:42.495235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6acad9f936f3'
down_revision = 'eab3d6b5798c'
branch_labels = None
depends_on = None


def upgrade():
    # Use batch mode to safely add the foreign key constraint
    with op.batch_alter_table('onboardings') as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_onboardings_employee_id', 'employees', ['employee_id'], ['id'])

    with op.batch_alter_table('reviews') as batch_op:
        batch_op.create_foreign_key('fk_reviews_employee_id', 'employees', ['employee_id'], ['id'])


def downgrade():
    with op.batch_alter_table('onboardings') as batch_op:
        batch_op.drop_constraint('fk_onboardings_employee_id', type_='foreignkey')
        batch_op.drop_column('employee_id')

    with op.batch_alter_table('reviews') as batch_op:
        batch_op.drop_constraint('fk_reviews_employee_id', type_='foreignkey')
