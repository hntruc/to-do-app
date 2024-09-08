# src/todoapp/backend/Dockerfile
FROM python:3.12-slim

# Set working directory
WORKDIR /app

COPY ../../pyproject.toml ../../poetry.lock /app/

# Install dependencies
RUN pip install poetry
RUN poetry install --no-root

# Copy backend source code
COPY . /app

# Install Alembic
RUN poetry add alembic

# Expose port
EXPOSE 8000

# Command to run Alembic migration
CMD ["sh", "-c", "poetry run alembic upgrade head"]