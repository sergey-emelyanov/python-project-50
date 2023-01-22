from gendiff.formatters import stylish_format, plain_format, json_format

FORMATTERS = {
    'stylish': stylish_format,
    'plain': plain_format,
    'json': json_format
}


def formatting(data, format_):
    if format_ not in FORMATTERS:
        raise ValueError("Unsupported format!")
    return FORMATTERS[format_].format(data)
