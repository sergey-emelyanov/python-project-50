install:
	poetry install

package-install:
	python -m pip install  dist/hexlet_code-0.1.0-py3-none-any.whl

package-reinstall:
	python -m pip install dist/hexlet_code-0.1.0-py3-none-any.whl --force-reinstall

build:
	poetry build
gendiff:
	 poetry run gendiff D:\pythonProject50\python-project-50\gendiff\\file1.json D:\pythonProject50\python-project-50\gendiff\\file2.json

