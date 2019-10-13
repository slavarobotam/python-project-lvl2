install:
	@poetry install

test:
	@poetry run pytest -vv

lint:
	@poetry run flake8

.PHONY: install test lint