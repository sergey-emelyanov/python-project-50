from gendiff.formatters.prepare_items import normalize_values


def stringify_val(data, depth: int) -> str:
    if not isinstance(data, dict):
        return data
    tmp = ["{"]
    for k, v in data.items():
        tmp.append(f"\n{'  ' * depth}  {k}: {stringify_val(v, depth + 2)}")
    tmp.append(f"\n{'  ' * (depth - 1)}}}")
    return ''.join(tmp)


def stringify_diff(diff: dict, depth=1) -> str:
    lst = []
    STATUS = {
        'unchanged': "  ",
        'add': "+ ",
        'del': "- "
    }

    for k, v in sorted(diff.items()):
        status = v['status']

        if status == 'nested':
            lst.append(f"{'  ' * depth}  {k}: {{\n")
            lst.append(f"{stringify_diff(v['value'], depth + 2)}")
            lst.append(f"{'  ' * (depth + 1)}}}\n")
        elif status == 'changed':
            lst.append(f"{'  ' * depth}- {k}: "
                       f"{stringify_val(v['old_value'], depth + 2)}\n")
            lst.append(f"{'  ' * depth}+ {k}: "
                       f"{stringify_val(v['new_value'], depth + 2)}\n")
        else:
            lst.append(f"{'  ' * depth}{STATUS[status]}{k}: "
                       f"{stringify_val(v['value'], depth + 2)}\n")
    res = ''.join(lst)
    return res


def format(diff: dict) -> str:
    diff = normalize_values(diff)
    return f"{{\n{stringify_diff(diff)}}}"
