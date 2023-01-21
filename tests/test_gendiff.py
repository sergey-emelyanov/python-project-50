import pytest
from gendiff import generate_diff
from tests.fixtures import ideal

correct_json = ideal.diff_json
correct_yaml = ideal.diff_yaml
correct_stylish = ideal.diff_stylish

json1 = r'tests/fixtures/file1.json'
json2 = r'tests/fixtures/file2.json'
json1nested = r'tests/fixtures/file1nested.json'
json2nested = r'tests/fixtures/file2nested.json'
yaml1 = r'tests/fixtures/file1.yaml'
yaml2 = r'tests/fixtures/file2.yaml'


def test_generate_diff_json():
    assert generate_diff(json1, json2) == correct_json


def test_generate_diff_yaml():
    assert generate_diff(yaml1, yaml2) == correct_yaml

def test_generate_diff_stylish():
    assert generate_diff(json1nested,json2nested,'stylish') == correct_stylish
