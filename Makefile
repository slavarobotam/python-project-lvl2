install:
	@poetry install

test:
	@poetry run pytest --cov=gendiff test_gendiff.py

lint:
	@poetry run flake8 --ignore=F401

.PHONY: install test lint