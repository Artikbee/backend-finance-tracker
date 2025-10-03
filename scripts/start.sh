#!/bin/sh
set -e

python -m alembic upgrade head
python -m uvicorn --factory src.main:create_app \
       --host $UVICORN_HOST \
       --port $UVICORN_PORT
