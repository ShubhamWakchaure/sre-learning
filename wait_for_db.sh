#!/bin/sh
set -e

host="${DB_HOST:-db}"
port="${DB_PORT:-5432}"

echo "⏳ Waiting for PostgreSQL at $host:$port..."

until pg_isready -h "$host" -p "$port" -U "$POSTGRES_USER"; do
  sleep 1
done

echo "✅ Postgres is ready!"
exec "$@"
