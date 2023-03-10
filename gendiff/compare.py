from gendiff.data import prepare_data
from gendiff.formatters.formatting import formatting
from gendiff.tree import make_diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    dict1 = prepare_data(file_path1)
    dict2 = prepare_data(file_path2)
    diff = make_diff(dict1, dict2)

    return formatting(diff, format_name)
