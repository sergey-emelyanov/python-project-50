import pytest
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


@pytest.mark.parametrize("test_input1,test_input2,formatter,expected",
                         [
                             pytest.param(json1, json2, 'stylish', correct_json),
                             pytest.param(yaml1, yaml2, 'stylish', correct_yaml),
                             pytest.param(json1nested, json2nested, 'stylish', correct_stylish),
                             pytest.param(yaml1nested, yaml2nested, 'stylish', correct_stylish_yaml),
                             pytest.param(json1nested, json2nested, 'plain', correct_plain),
                             pytest.param(yaml1nested, yaml2nested, 'plain', correct_plain_yaml),
                             pytest.param(json1nested, json2nested, 'json', correctjson_json),
                             pytest.param(yaml1nested, yaml2nested, 'json', correctyaml_json)

                         ]
                         )
def test_generate_diff(test_input1, test_input2, formatter, expected):
    assert generate_diff(test_input1, test_input2, formatter) == expected
