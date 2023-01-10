from gendiff import generate_diff

diff_json = generate_diff(r'tests/fixtures/file1.json',
                          r'tests/fixtures/file2.json')

diff_yaml = generate_diff(r'tests/fixtures/file1.yaml',
                          r'tests/fixtures/file2.yaml')
