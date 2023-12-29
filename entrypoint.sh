#!/bin/bash
set -e

# Wait for the Postgres database to be ready
dockerize -wait tcp://db:5432 -timeout 60s

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Start the application
echo "Starting server..."
exec "$@"
