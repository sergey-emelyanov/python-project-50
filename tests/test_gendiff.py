import pytest
from gendiff import generate_diff
from tests.fixtures import ideal

correct = ideal.diff

json1 = r'tests/fixtures/file1.json'
json2 = r'tests/fixtures/file2.json'


def test_generate_diff():
    assert generate_diff(json1, json2) == correct
