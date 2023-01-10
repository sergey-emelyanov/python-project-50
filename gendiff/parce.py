import json
import yaml


def parcing(data, format):
    if format == 'yaml' or format == 'yml':
        return yaml.safe_load(data)
    if format == 'json':
        return json.loads(data)
