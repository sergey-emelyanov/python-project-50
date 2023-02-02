import json
import yaml

EXTENSIONS = ('yaml', 'yml', 'json')


def what_format(file_path):
    extension = file_path.split('.')[1]
    return extension


def open_json(file_path):
    data = json.load(open(file_path))
    return data


def open_yaml(file_path):
    data = yaml.safe_load(open(file_path))
    return data


def prepare_data(file_path):
    extension = what_format(file_path)
    if extension == 'json':
        data = open_json(file_path)
        return data
    elif extension == 'yaml' or extension == 'yml':
        data = open_yaml(file_path)
        return data
    else:
        raise Exception("Unsupported type of file")
