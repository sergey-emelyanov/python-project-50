import json


def prepare_boolean(value):
    if value == True:
        return 'true'
    elif value == False:
        return 'false'
    return value


def generate_diff(file_path1, file_path2):
    diff = []
    diff.append('{')
    dict1 = json.load(open(file_path1))
    dict2 = json.load(open(file_path2))
    all_keys = sorted(set(dict1) | set(dict2))

    for i in all_keys:
        if dict2.get(i) is None:
            diff.append(f"{'-'} {i}: {prepare_boolean(dict1[i])}")
        elif dict1.get(i) is None:
            diff.append(f"{'+'} {i}: {prepare_boolean(dict2[i])}")
        elif dict1[i] != dict2[i]:
            diff.append(f"{'-'} {i}: {prepare_boolean(dict1[i])}")
            diff.append(f"{'+'} {i}: {prepare_boolean(dict2[i])}")
        elif dict1[i] == dict2[i]:
            diff.append(f"{' '} {i}: {prepare_boolean(dict1[i])}")

    diff.append('}')

    return '\n'.join(diff)
