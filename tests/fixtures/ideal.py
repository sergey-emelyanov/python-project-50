from gendiff import generate_diff

diff_json = generate_diff(r'tests/fixtures/file1.json',
                          r'tests/fixtures/file2.json')

diff_yaml = generate_diff(r'tests/fixtures/file1.yaml',
                          r'tests/fixtures/file2.yaml')

diff_stylish = generate_diff(r'tests/fixtures/file1nested.json',
                             r'tests/fixtures/file2nested.json', 'stylish')

diff_stylish_yaml = generate_diff(r'tests/fixtures/file1nested.yaml',
                                  r'tests/fixtures/file2nested.yaml', 'stylish')

diff_plain = generate_diff(r'tests/fixtures/file1nested.json',
                           r'tests/fixtures/file2nested.json', 'plain')

diff_plain_yaml = generate_diff(r'tests/fixtures/file1nested.yaml',
                                r'tests/fixtures/file2nested.yaml', 'plain')

diffjson_json = generate_diff(r'tests/fixtures/file1nested.json',
                              r'tests/fixtures/file2nested.json', 'json')

diffyaml_json = generate_diff(r'tests/fixtures/file1nested.yaml',
                              r'tests/fixtures/file2nested.yaml', 'json')
