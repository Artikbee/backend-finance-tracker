UVICORN_HOST=127.0.0.1
UVICORN_PORT=8000

run:
	python -m uvicorn --factory src.main:create_app --host $(UVICORN_HOST) --port $(UVICORN_PORT) --reload

migrations:
	alembic revision --autogenerate

migrate:
	alembic upgrade head

deps:
	uv pip install -e ".[dependencies,lint,test]"

ruff:
	ruff check src/

test:
	pytest -v