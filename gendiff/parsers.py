import json
import yaml
import os


def parse_file(file_path):
    extension = os.path.splitext(file_path)[-1][1:]
    if extension == 'yaml' or 'yml':
        return yaml.load(open(file_path), Loader=yaml.FullLoader)
    elif extension == 'json':
        return json.load(open(file_path))
