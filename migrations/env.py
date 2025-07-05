from logging.config import fileConfig
import os
from sqlalchemy import create_engine, pool
from alembic import context
from dotenv import load_dotenv

# Load env vars from .env.local
load_dotenv(dotenv_path=".env.local")

# This is the Alembic Config object
config = context.config

# Setup logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Import your models and metadata
from app.db import Base  # Make sure this is correct
from app import models   # This makes sure all models are loaded

target_metadata = Base.metadata

# Get DB URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

# Support SQLite's special needs
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    engine = create_engine(DATABASE_URL, connect_args=connect_args, poolclass=pool.NullPool)

    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
