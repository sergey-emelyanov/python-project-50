from gendiff.data import prepare_data
from gendiff.parce import parcing
from gendiff.formatters.stylish_format import format
from gendiff.tree import make_diff


def generate_diff(file_path1, file_path2, format_style='stylish'):
    data1, format1 = prepare_data(file_path1)
    data2, format2 = prepare_data(file_path2)
    dict1 = parcing(data1, format1)
    dict2 = parcing(data2, format2)

    diff = make_diff(dict1, dict2)

    return format(diff)
