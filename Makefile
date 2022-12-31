install:
	poetry install

package-install:
	python -m pip install  dist/hexlet_code-0.1.0-py3-none-any.whl

package-reinstall:
	python -m pip install dist/hexlet_code-0.1.0-py3-none-any.whl --force-reinstall

build:
	poetry build

