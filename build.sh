#!/usr/bin/env bash
# Exit on error
set -o errexit

# Print commands as they are executed
set -x

# Install dependencies
pip install -r requirements.txt

# Make sure static directory exists
mkdir -p staticfiles

# Convert static asset files
python manage.py collectstatic --noinput

# Apply any outstanding database migrations
python manage.py migrate

# Start Gunicorn with the config file
gunicorn config.wsgi:application --config gunicorn_config.py