def make_diff(old: dict, new: dict):  # noqa:  C901
    result = {}

    deleted_keys = set(sorted(old.keys())) - set(sorted(new.keys()))
    for key in deleted_keys:
        result[key] = {'status': 'del', 'value': old[key]}

    added_keys = set(sorted(new.keys())) - set(sorted(old.keys()))
    for key in added_keys:
        result[key] = {'status': 'add', 'value': new[key]}

    both_keys = set(sorted(old.keys())) & set(sorted(new.keys()))
    for key in both_keys:
        old_value = old[key]
        new_value = new[key]
        if isinstance(old_value, dict) and isinstance(new_value, dict):
            result[key] = {'status': 'nested',
                           'value': make_diff(old_value, new_value)}
        elif old_value == new_value:
            result[key] = {'status': 'unchanged', 'value': old_value}
        elif old_value != new_value:
            result[key] = {'status': 'changed',
                           'old_value': old_value, 'new_value': new_value}

    return result
