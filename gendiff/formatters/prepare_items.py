def normalize_values(data: dict) -> dict:
    correct_values = {None: 'null', True: 'true', False: 'false'}

    for key, val in data.items():
        if isinstance(val, dict):
            normalize_values(val)
        elif isinstance(val, (bool, type(None))):
            data[key] = correct_values[val]
    return data
