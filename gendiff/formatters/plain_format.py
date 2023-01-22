def stringify_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, type(None)):
        return 'null'
    if isinstance(value, int):
        return str(value)
    if isinstance(value, (dict, list, tuple)):
        return '[complex value]'
    return f"'{value}'"


def plain_format(diff, father_key=''):  # noqa:  C901
    result = []
    for key, value in sorted(diff.items()):
        if len(father_key) > 1:
            key = father_key + '.' + key
        if value['status'] == 'nested':
            result.extend(plain_format(value['value'], key))
        elif value['status'] == 'del':
            result.append(f"Property '{key}' was removed")
        elif value['status'] == 'add':
            result.append(f"Property '{key}' was added with value: "
                          f"{stringify_value(value['value'])}")
        elif value['status'] == 'changed':
            result.append(
                f"Property '{key}' was updated. "
                f"From {stringify_value(value['old_value'])} to"
                f" {stringify_value(value['new_value'])}")

    return result


def format(diff: dict) -> str:
    diff = plain_format(diff)
    return '\n'.join(diff)
