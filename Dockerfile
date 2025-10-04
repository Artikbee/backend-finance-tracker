FROM ghcr.io/astral-sh/uv:python3.10-bookworm-slim AS builder

WORKDIR /app

COPY ./pyproject.toml ./pyproject.toml
COPY ./scripts/start.sh ./alembic.ini ./
COPY ./src ./src

RUN uv pip install --system --no-cache --target dependencies .

FROM python:3.10-slim as production

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "/app/dependencies"

RUN apt-get update && apt-get install -y curl

COPY --from=builder /app/ ./