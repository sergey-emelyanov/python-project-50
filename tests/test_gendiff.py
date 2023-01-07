import pytest
from gendiff import generate_diff
from tests.fixtures import ideal

correct = ideal.diff

json1 = r'D:\pythonProject50\python-project-50\tests\fixtures\file1.json'
json2 = r'D:\pythonProject50\python-project-50\tests\fixtures\file2.json'


def test_generate_diff():
    assert generate_diff(json1, json2) == correct
