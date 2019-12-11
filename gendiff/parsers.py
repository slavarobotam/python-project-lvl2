import json
import yaml
import os


def _get_extension(file_path):
    return os.path.splitext(file_path)[-1][1:]


def _read_data_from_file(file_path, extension):
    if extension == 'yaml' or 'yml':
        return yaml.load(open(file_path), Loader=yaml.FullLoader)
    elif extension == 'json':
        return json.load(open(file_path))


def get_parsed_data(filepath):
    extension = _get_extension(filepath)
    raw_data = _read_data_from_file(filepath, extension)
    return raw_data
