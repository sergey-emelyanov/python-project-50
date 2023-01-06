import pytest
from gendiff import generate_diff


json1 = 'D:\pythonProject50\python-project-50\\tests\\fixtures\\file1.json'
json2 = 'D:\pythonProject50\python-project-50\\tests\\fixtures\\file2.json'


def test_generate_diff():
    assert generate_diff(json1, json2) == '''
    {
    - follow: false
      host: hexlet.io
    - proxy: 123.234.53.22
    - timeout: 50
    + timeout: 20
    + verbose: true
    }
    '''

