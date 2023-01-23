import json
import yaml
EXTENSIONS = ('yaml', 'yml', 'json')


def prepare_data(file_path):
    extension = file_path.split('.')[1]
    if extension == 'json':
        data = json.load(open(file_path))
        return data
    elif extension == 'yaml' or extension == 'yml':
        data = yaml.safe_load(open(file_path))
        return data

