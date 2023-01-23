import json
from gendiff.formatters.prepare_items import normalize_values


def format(diff):
    diff = normalize_values(diff)
    diff = dict(sorted(diff.items(), key=lambda x: x[0]))
    return json.dumps(diff, indent=4)
