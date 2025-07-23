#!/bin/sh
set -e

# Default values (can override via environment)
hosts="${FASTAPI_HOSTS:-fastapi-web-server-1 fastapi-web-server-2}"
port="${FASTAPI_PORT:-8000}"
path="${FASTAPI_PATH:-/healthcheck}"

for host in $hosts; do
  url="http://$host:$port$path"
  echo "⏳ Waiting for FastAPI at $url..."

  until curl --silent --fail "$url"; do
    echo "❌ $host not ready yet..."
    sleep 1
  done

  echo "✅ $host is ready!"
done

exec "$@"
