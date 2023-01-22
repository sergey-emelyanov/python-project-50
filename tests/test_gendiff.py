from gendiff import generate_diff
from tests.fixtures import ideal

correct_json = ideal.diff_json
correct_yaml = ideal.diff_yaml
correct_stylish = ideal.diff_stylish
correct_stylish_yaml = ideal.diff_stylish_yaml
correct_plain = ideal.diff_plain
correct_plain_yaml = ideal.diff_plain_yaml
correctjson_json = ideal.diffjson_json
correctyaml_json = ideal.diffyaml_json

json1 = r'tests/fixtures/file1.json'
json2 = r'tests/fixtures/file2.json'
json1nested = r'tests/fixtures/file1nested.json'
json2nested = r'tests/fixtures/file2nested.json'
yaml1 = r'tests/fixtures/file1.yaml'
yaml2 = r'tests/fixtures/file2.yaml'
yaml1nested = r'tests/fixtures/file1nested.yaml'
yaml2nested = r'tests/fixtures/file2nested.yaml'


def test_generate_diff_json():
    assert generate_diff(json1, json2) == correct_json


def test_generate_diff_yaml():
    assert generate_diff(yaml1, yaml2) == correct_yaml


def test_generate_diff_stylish():
    assert generate_diff(json1nested, json2nested, 'stylish') == correct_stylish


def test_generate_diff_stylish_yaml():
    assert generate_diff(yaml1nested, yaml2nested, 'stylish') == correct_stylish_yaml


def test_generate_diff_plain():
    assert generate_diff(json1nested, json2nested, 'plain') == correct_plain


def test_generate_diff_plain_yaml():
    assert generate_diff(yaml1nested, yaml2nested, 'plain') == correct_plain_yaml


def test_generate_diff_json_json():
    assert generate_diff(json1nested, json2nested, 'json') == correctjson_json


def test_generate_diff_yaml_json():
    assert generate_diff(yaml1nested, yaml2nested, 'json') == correctyaml_json
