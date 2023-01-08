install:
	poetry install
package-install:
	python -m pip install  dist/hexlet_code-0.1.0-py3-none-any.whl
package-reinstall:
	python -m pip install dist/hexlet_code-0.1.0-py3-none-any.whl --force-reinstall
build:
	poetry build
lint:
	poetry run flake8 gendiff
pytest:
	poetry run pytest
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

