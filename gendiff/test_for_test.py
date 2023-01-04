from gendiff import generate_diff

diff = generate_diff('D:\pythonProject50\python-project-50\gendiff\\file1.json',
                     'D:\pythonProject50\python-project-50\gendiff\\file2.json')
print(diff)

diff2 = generate_diff('file1.json', 'file2.json')
print(diff2)
