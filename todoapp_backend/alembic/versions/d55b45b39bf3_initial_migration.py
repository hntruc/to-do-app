"""Add some_table

Revision ID: d55b45b39bf3
Revises: 
Create Date: 2024-09-06 16:33:45.542159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd55b45b39bf3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Tạo bảng mới
    op.create_table(
        'todos',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('task', sa.String, nullable=False),
        sa.Column('done', sa.Boolean, nullable=False)
    )
    
    # Chèn dữ liệu vào bảng mới
    op.bulk_insert(
        sa.table(
            'todos',
            sa.Column('id', sa.Integer),
            sa.Column('task', sa.String),
            sa.Column('done', sa.Boolean)
        ),
        [
            {'id': 1, 'task': 'Task 1: Prepare env', 'done': True},
            {'id': 2, 'task': 'Task 2: Run data migration', 'done': False}
        ]
    )


# def downgrade():
#     # Xóa bảng
#     op.drop_table('some_table')