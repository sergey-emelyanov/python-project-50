EXTENSIONS = ('yaml', 'yml', 'json')


def prepare_data(file_path):
    extension = file_path.split('.')[1]
    if extension in EXTENSIONS:
        with open(file_path) as f:
            data = f.read()
    return data, extension
