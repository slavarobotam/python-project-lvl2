install:
	@poetry install

test:
	@poetry run pytest -vv --cov=gendiff tests/ --cov-report xml

lint:
	@poetry run flake8 --ignore=F401

complex:  # test run with complex json
	@poetry run gendiff -f plain tests/fixtures/complex_before.json tests/fixtures/complex_after.json

json:  # test run with plain json
	@poetry run gendiff -f plain tests/fixtures/before.json tests/fixtures/after.json

yaml:  # test run with plain yaml
	@poetry run gendiff -f plain tests/fixtures/before.yml tests/fixtures/after.yml

all:
	make json
	make yaml
	make complex
.PHONY: install test lint