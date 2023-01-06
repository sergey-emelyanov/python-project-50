from gendiff import generate_diff

diff1 = generate_diff('D:\pythonProject50\python-project-50\\tests\\fixtures\\file1.json',
                      'D:\pythonProject50\python-project-50\\tests\\fixtures\\file2.json')
print(diff1)